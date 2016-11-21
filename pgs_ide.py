import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import tkinter.filedialog as tkfd
from pathlib2 import Path
from interpreter import RunPage

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
            
        frame = MainPage(self.container, self)
        self.frames["MainPage"] = frame

        frame.grid(row=0,column=0,sticky="nsew")

        frame = RunPage(self.container, self)
        self.frames["RunPage"] = frame

        frame.grid(row=0,column=0,sticky="nsew")

        # Set the starting page
        self.show_frame("MainPage")

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

    def get_code(self):
        return self.frames["MainPage"].textArea.get("1.0",tk.END)

    def run(self):
        self.show_frame("RunPage")
        self.frames["RunPage"].run(self.get_code())

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

        self.name = "MainPage"

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
        self.runMenu.add_command(label="Run Script", command=self.controller.run)

        # Create a 'help' menu
        self.helpMenu = tk.Menu(self.menubar)
        self.helpMenu.add_command(label="PigeonScript Docs", command=None)

        # Add the file menu to the window
        self.menubar.add_cascade(label="File", menu=self.fileMenu)
        self.menubar.add_cascade(label="Run", menu=self.runMenu)
        self.menubar.add_cascade(label="Help", menu=self.helpMenu)
    
app = pgsIDEApp()
app.mainloop()
