# This is the PigeonScript interpreter

from pgn_parser import parse

# Take user input and parse it

code = input("Input your program:\n")

instructions = parse(code)

'''
I'm just laying out my thoughts here.

A loop will iterate through the list of parsed instrucions, and executes each one as it goes along.
Functions will be executed in a function that will run recursively, so that loops within the program
will be able to run within that single function.
'''

def execute(instruction):
    if instruction
