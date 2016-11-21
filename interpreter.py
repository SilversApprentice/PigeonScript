import math

from pgs-functions import *

global stack
stack = []

def run(code):

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

    nonreturn = {'p':prnt,
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
    instructions = parse(code)
    execute(instructions)
