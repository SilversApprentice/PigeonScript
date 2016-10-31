# This is the PigeonScript interpreter

from pgn_parser import parse

# Take user input and parse it

code = input("Input your program:\n")

parse(code)
