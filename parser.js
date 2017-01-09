// This file will parse the script

var stack = []

//toNum converts a String to a Number if possible, and if not it leaves it as a String.

var toNum = function(input){
    if(isNaN(Number(input))){
        return input
    } else {
        return Number(input)
    }
}

var pop = function(amount) {
    if(stack.length){
        return stack.pop()
    } else {
        return toNum(prompt("This PigeonScript application is requesting input."))
    }
}

var sum = function() {
    if(stack.length)
       return pop() + pop()
    else
       return pop() * 2
}

var sub = function() {
    if(stack.length)
        return -1 * (pop() - pop()) 
    else 
        return -1 * pop()
}

var mult = function() {
    if(stack.length)
        return pop() * pop()
    else
        return pow(pop(), 2)
}

var div = function() {
    if(stack.length)
        return 1 / (pop() / pop())
    else
        return 1 / pow()
}

var alias = {
    "+" : sum,
    "-" : sub,
    "*" : mult,
    "/" : div,
    "?" : prompt
}

var validCommands = "+-*/?"

var temp = ""

var code = prompt("Program")
for (var i = 0; i < code.length; ++i) {
    if(validCommands.indexOf(code[i]) + 1){
        if(temp.length){
            stack.push(toNum(temp))
            temp = ""
        }
        stack.push(alias[code[i]]())
    } else {
        temp += code[i]
    }
}

if(temp.length) stack.push(toNum(temp))

alert(stack.pop()) //We need an "infinite loop" command so that you can disable implicit output

if(stack.length) alert("WARNING: Items were left on the stack!")
