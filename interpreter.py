import tkinter as tk
from tkinter.scrolledtext import ScrolledText

from pgs_funcs import *

class RunPage(tk.Frame):
    
    def run(self, code):

        if code.count('"') % 2 == 1:
            code = '"' + code # implicit opening brackets
        instructions = parse(code)
        execute(instructions)
