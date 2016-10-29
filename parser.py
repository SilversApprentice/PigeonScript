
# Parser for PigeonScript

# 33Aw1Ɓ;i0;+
# becomes
# [
#   ("pushint", 33),
#   ("setvar", "a"),
#   ("control", "whileLoop", [
#     ("pushint", 1)
#     ("control", "break")
#   ]),
#   ("control", "if", [
#     ("pushint", 0)
#   ]),
#   ("instruction", "add")
# ]

digits = list("0123456789")
get_var = list("abcdef")
set_var = list("ABCDEF")

# parse the chars.txt file to get the list of instructions
with open("chars.txt", "r") as f:

	linelist = [line.rstrip("\n") for line in f]
	
	# the characters which are instructions
	# ignore the first line, which is a title
	instructionsRaw = linelist[1:linelist.index("CONTROL")]
	instructions = {}
	
	for i in instructionsRaw:
		line = i.split(" ")
		if len(line) != 2:
			raise RuntimeError("File parse error")
		
		instructions[line[0]] = line[1]
	
	# the character which are for control
	# each character is represented as a tuple of its name and a bool of whether it has a body (like a loop)
	controlRaw = linelist[linelist.index("CONTROL") + 1:]
	control = {}
	
	for i in controlRaw:
		line = i.split(" ")
		if len(line) == 2:
			control[line[0]] = (line[1], False)
		elif len(line) == 3 and line[2] == "{}":
			control[line[0]] = (line[1], True)
		else:
			raise RuntimeError("File parse error")
			
# end file parse
# the variables instructions and control are now important

def parse(code): # a recursive function to parse code
	
	pointer = 0
	c = lambda: code[pointer]
	parsed = []
	
	while pointer < len(code):
		
		# parse this as a number
		if c() in digits:
			
			number = ""
			
			while pointer < len(code) and c() in digits:
				number += c()
				pointer += 1
				
			pointer -= 1
			parsed.append(("pushnum", int(number)))
			
		# parse this as a variable name
		elif c() in get_var:
			
			name = ""
			
			while pointer < len(code) and c() in get_var:
				name += c()
				pointer += 1
				
			pointer -= 1
			parsed.append(("pushvar", name))
			
		# parse this as a variable name
		elif c() in set_var:
			
			name = ""
			
			while pointer < len(code) and c() in set_var:
				name += c()
				pointer += 1
				
			pointer -= 1
			parsed.append(("setvar", name))
			
		# parse this as an instruction
		elif c() in instructions:
			
			parsed.append(("instruction", instructions[c()]))
			
		# parse this as a control character
		elif c() in control:
			
			# Ha ha, control[c]
			if control[c()][1]:
				
				# save this for later
				char = c()
				
				# parse everything from here to the next semicolon (or EOF) as code
				innerCode = ""
				
				pointer += 1
				while pointer < len(code) and c() != ";":
					innerCode += c()
					pointer += 1
					
				pointer -= 1	
				parsed.append(("control", control[char][0], parse(innerCode)))
				
			else:
				parsed.append(("control", control[c()][0]))
				
		
		pointer += 1
	
	return parsed
