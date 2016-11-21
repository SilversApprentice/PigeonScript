import tkinter as tk
from tkinter.scrolledtext import ScrolledText

from pgs_funcs import *

class RunPage(tk.Frame):

    '''
    This is all content on the RunPage
    '''

    def __init__(self, parent, controller):

        ''' Constructor '''

        # Call the parents constructor
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

        self.name = "RunPage"
        
        # Add the content

        # Create an output text box
        self.outBox = ScrolledText(self)
        self.outBox.pack(side="top")

        # Just a label
        self.errorBoxLabel = tk.Label(self, text="Error Messages:")
        self.errorBoxLabel.pack()

        # Create an error box
        self.errorBox = ScrolledText(self)
        self.errorBox.pack(side="top")

        # Create the menu
        self.menuBar = tk.Menu(self.controller)
        self.set_menubar = lambda: self.controller.config(menu=self.menuBar)

        # Create a 'file' menu
        self.fileMenu = tk.Menu(self.menuBar)
        self.fileMenu.add_command(label="New", command=self.controller.create_new)
        self.fileMenu.add_command(label="Open", command=
                                  lambda: self.controller.create_new(self.controller.open_file())
                                  )
        self.fileMenu.add_command(label="Quit", command=self.controller.quit)

        # Create a 'debug' menu
        self.debugMenu = tk.Menu(self.menuBar)
        self.debugMenu.add_command(label="Quit", command=None)

        # Create a 'window' menu
        self.windowMenu = tk.Menu(self.menuBar)
        self.windowMenu.add_command(label="Return to Editor", command=
                                    lambda: self.controller.show_frame("MainPage")
                                    )

        # Add the menus to the window
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.menuBar.add_cascade(label="Debug", menu=self.debugMenu)
        self.menuBar.add_cascade(label="Window", menu=self.windowMenu)

    def prnt(self):
        # This needs to be in this file since it outputs to the console
        a=pop()
        print(a)
        self.outBox.insert(tk.END, a) # WIP
    
    def parse(self, code):
    
        pointer = 0

        c = lambda: code[pointer]

        parsed = []

        while pointer < len(code):

            if c() in digits:

                number = ""

                while pointer < len(code) and (c() in digits or (c() == '.' and '.' not in number)):
                    number += c()
                    pointer += 1
                pointer -= 1
                parsed.append(("push", cast(number)))

            if c() == '"':

                string = ""

                while pointer < len(code):
                    string += c()
                    pointer += 1
                    if pointer >= len(code) or c() == '"':
                        break
                parsed.append(("push", string.strip('"')))

            elif c() in functions:
                parsed.append(("function", functions[c()]))

            elif c() in nonreturn:
                parsed.append(("nonreturn", nonreturn[c()]))

            elif c() in set_var:
                parsed.append(("setvar", c().lower()))

            elif c() in get_var:
                parsed.append(("getvar", c()))

            elif c() in constants:
                parsed.append(("push", constants[c()]))

            elif c() in control:

                if control[c()][1]:

                    char = c()

                    innerCode = ""

                    nest = 1
                    while pointer + 1 < len(code) or nest > 0:
                        pointer += 1
                        innerCode += c()
                        if c() in control:
                            nest += 1
                        elif c() == ";":
                            nest -= 1
                        if nest <= 0:break

                    innerCode = innerCode[0:-1]

                    parsed.append(("control", control[char][0], parse(innerCode)))

                else:

                    parsed.append(("control", control[c()][0]))
                
            pointer += 1

        return parsed

    def execute(self, code):

        pointer = 0
        c = lambda: code[pointer]

        while pointer < len(code):

            if c()[0] == "push":
                stack.append(c()[1])

            elif c()[0] == "function":
                stack.append(c()[1]())

            elif c()[0] == "nonreturn":
                c()[1]()

            elif c()[0] == "setvar":
                if isinstance(scope[c()[1]], list):
                    a = pop()
                    if type(a) == str:
                        if "|" in a:
                            b = (a.split("|"))
                            for d in b:
                                scope[c()[1]] += [d]
                        else:
                            scope[c()[1]].append(a)
                    if type(a) == int or type(a) == float:
                        for b in range(len(to_append)):
                            scope[c()[1]] += [to_append.pop(0)]
                        scope[c()[1]].append(a)
                else:
                    scope[c()[1]] = pop()

            elif c()[0] == "getvar":
                stack.append(scope[c()[1]])
                
            elif c()[0] == "control":
                
                if c()[1] == "if":
                    if pop():execute(c()[2])

                elif c()[1] == "forLoop":
                    a = pop()

                    if type(a) == list or type(a) == str:
                        for n in range(len(a)):execute(c()[2])
                    else:
                        for n in range(a):execute(c()[2])
                    
            pointer += 1

        if len(stack):self.outBox.insert("1.0", stack[-1])
    
    def run(self, code):
        
        # link functions to their characters
        global digits, set_var, get_var, functions, nonreturn, constants, control
        digits = list("0123456789")
        set_var = list("ABCDEF")
        get_var = list("abcdef")

        functions = {'+':add,
                     '-':sub,
                     '*':mult,
                     '/':div,
                     '^':exp,
                     '%':mod,
                     '~':indice,
                     'l':length,
                     '=':equals,
                     '>':morethan,
                     '<':lessthan,
                     '&':booland,
                     'o':boolor,
                     '!':boolnot}

        nonreturn = {'p':self.prnt,
                     '|':pshtoarr}

        constants = {'g':[]}

        control = {'i': ('if', True),
                   'w': ('whileLoop', True),
                   'y': ('forLoop', True)}

        to_append = []

        # vars the user has access to

        scope = {'a':0,
                 'b':0,
                 'c':0,
                 'd':0,
                 'e':0,
                 'f':"Hello World"} # this makes the hello world program nice and short...

        if code.count('"') % 2 == 1:
            code = '"' + code # implicit opening brackets
        instructions = self.parse(code)
        self.execute(instructions)
