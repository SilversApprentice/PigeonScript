import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import tkinter.filedialog as tkfd
from pathlib2 import Path
import interpreter

class pgsIDEApp(tk.Tk):

    '''
    This is the main backend class
    '''

    def __init__(self, content=""):

        ''' Constructor '''

        # Call the parents constructor
        tk.Tk.__init__(self)

        # Set the window title
        tk.Tk.wm_title(self, "Pigeon IDE")

        # Set the window size
        self.geometry('{}x{}'.format(800,600))

        # Store the starting content (for when opening files)
        self.content = content

        # If the file has been saved before...
        self.has_saved = False
        # ...and where it was saved to
        self.saved_path = None
        
        # Create the container
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        # And configure the grid
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Create a dictionary of frames and append all pages to it
        self.frames = {}

        for f in (MainPage, RunPage):
            
            frame = f(self.container, self)
            self.frames[f] = frame

            frame.grid(row=0,column=0,sticky="nsew")

        # Set the starting page
        self.show_frame(MainPage)

    def show_frame(self, cont):

        # A simple function to switch pages

        frame = self.frames[cont]
        frame.tkraise()
        frame.set_menubar()

    def create_new(self, content=""):

        # Creates another isntance of this class to have multiple files open at once
        newApp = pgsIDEApp(content)
        newApp.mainloop()

    def open_file(self):
        opennm = tkfd.askopenfile()
        if not opennm == None:
            f = Path(opennm.name).read_text()
            self.has_saved = True
            self.saved_path = opennm.name
            return f
        else:
            return ""

    def save_file(self, data, overwrite=False):

        if overwrite and self.controller.has_saved:
            f = open(self.controller.saved_path, 'w')        
        else:
            f = tkfd.asksaveasfile(mode="w")
        if f is None:
            # If dialogue was closed by the 'cancel'
            return
        f.write(data)
        self.controller.has_saved = True
        self.controller.saved_path = f.name
        f.close()

    def quit(self):
        self.destroy()

class MainPage(tk.Frame):

    '''
    This is all the content on the main page
    '''

    def __init__(self, parent, controller):

        ''' Constructor '''

        # Call the parents constructor
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

        # Add the content
        
        # Fill the whole window with a text box to be typed into
        self.textArea = ScrolledText(self)
        self.textArea.pack(side="top", fill="both", expand=True)
        
        self.textArea.insert(tk.INSERT, self.controller.content)

        # Create the menubar and add it to the parent window
        self.menubar = tk.Menu(self.controller)
        self.set_menubar = lambda: self.controller.config(menu=self.menubar)

        # Create a 'file' menu
        self.fileMenu = tk.Menu(self.menubar)
        self.fileMenu.add_command(label="New", command=self.controller.create_new)
        self.fileMenu.add_command(label="Open", command=
                             lambda: self.controller.create_new(self.controller.open_file())
                             )
        self.fileMenu.add_command(label="Save", command=
                             lambda: self.controller.save_file(self.textArea.get(1.0,tk.END),True)
                             )
        self.fileMenu.add_command(label="Save As", command=
                             lambda: self.controller.save_file(self.textArea.get(1.0,tk.END))
                             )
        self.fileMenu.add_command(label="Quit", command=self.controller.quit)

        # Create a 'run' menu
        self.runMenu = tk.Menu(self.menubar)
        self.runMenu.add_command(label="Run Script", command=
                            lambda: self.controller.show_frame(RunPage)
                            )

        # Create a 'help' menu
        self.helpMenu = tk.Menu(self.menubar)
        self.helpMenu.add_command(label="PigeonScript Docs", command=None)

        # Add the file menu to the window
        self.menubar.add_cascade(label="File", menu=self.fileMenu)
        self.menubar.add_cascade(label="Run", menu=self.runMenu)
        self.menubar.add_cascade(label="Help", menu=self.helpMenu)

class RunPage(tk.Frame):

    '''
    This is all the content on the RunPage
    '''

    def __init__(self, parent, controller):

        ''' Contstructor '''

        # Call the parents constructor
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

        # Add the content

        # Create an output text box
        self.outBox = ScrolledText(self)
        self.outBox.pack(side="top")
        self.outBox.config(state=tk.DISABLED)

        # Just a label
        self.errorBoxLabel = tk.Label(self, text="Error Messages:")
        self.errorBoxLabel.pack()
        
        # Create an error box
        self.errorBox = ScrolledText(self)
        self.errorBox.pack(side="top")
        self.errorBox.config(state=tk.DISABLED)

        # Create the menu
        self.menubar = tk.Menu(self.controller)
        self.set_menubar = lambda: self.controller.config(menu=self.menubar)

       # Create a 'file' menu
        self.fileMenu = tk.Menu(self.menubar)
        self.fileMenu.add_command(label="New", command=self.controller.create_new)
        self.fileMenu.add_command(label="Open", command=
                             lambda: self.controller.create_new(self.controller.open_file())
                             )
        self.fileMenu.add_command(label="Quit", command=self.controller.quit)

        # Create a 'debug' menu
        self.debugMenu = tk.Menu(self.menubar)
        self.debugMenu.add_command(label="Show parsed code", command=None)

        # Create a 'window' menu
        self.windowMenu = tk.Menu(self.menubar)
        self.windowMenu.add_command(label="Return To Editor", command=
                               lambda: self.controller.show_frame(MainPage)
                               )

        # Add the file menu to the window
        self.menubar.add_cascade(label="File", menu=self.fileMenu)
        self.menubar.add_cascade(label="Debug", menu=self.debugMenu)
        self.menubar.add_cascade(label="Window", menu=self.windowMenu) 
    
app = pgsIDEApp()
app.mainloop()
