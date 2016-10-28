# Instruction Listings #

## Instructions ##

- `+` (2 inputs)
  - *int, int*: adds two integers: `1,1` -> `2`
  - *array, array*: concantenates two arrays: `[1,2,3],[4,5,6]` -> `[1,2,3,4,5,6]`
  - *ASCII-art, ASCII-art*: horizontally concatenates two ASCII-arts: `{"ab","cd"},{"12","34"}` -> `{"ab12","cd34"}`
- `±` (2 inputs)
  - *int, int*: subtracts two integers: `3,1` -> `2`.
  - *array, **: appends into the array: `[1,2],3` -> `[1,2,3]`
  - *ASCII-art, ASCII-art*: vertically concatenates two ASCII-arts: `{"ab","cd"},{"12","34"}` -> `{"ab", "cd", "12", "34"}`
- `N` (0 inputs)
  - Input an integer and push it onto the stack: `1,2` -> `1,2,3`
- `Ñ` (0 inputs)
  - Input a list of integers: `1,2` -> `1,2,[3,4,5]`
- `ñ` (0 inputs)
  - Input a one-line ASCII art (a string): `{"spam","eggs"}` -> `{"spam","eggs"},{"foo"}`
- `ã` (0 inputs)
  - Input an ASCII-art: `1,2,3` -> `1,2,3,{"spam","eggs"}`
- `ń` (0 inputs)
  - If the `ń` command has not been run before, input an integer and push it onto the stack. Otherwise, push the input
    onto the stack: `1,2,3` -> `1,2,3,4` -> `1,2,3,4,4`
- `|` (0 inputs)
  - Skip to the next newline (used for comments).
  
## Control Structures ##

- `W...;`
  - While the top element on the stack has a truthy value (number > 1, non-empty list/ASCII art)
- `U...;`
  - Until the top element on the stack has a truthy value
- `F[name]...;` (`[name]` is a variable name)
  - Take a value `t` from the top of the stack. If `t` is an int, this is equivalent to `for (var [name] = 0;
    n < t; n++) {...}`. If `t` is an array, this is equivalent to `foreach (t as [name]) {...}`.
- `ƒ...;`
  - Like `F`, but automatically uses the variable `n` for `[name]`. If `n` is already used, keep going
    alphabetically until it finds an unused character. (`o`, `p`, ... `z`, `aa`, `ab`)
- `D[name]...;` (`[name]` is a variable name)
  - Pop a value `d`. `[name]` will loop through every possible value for a `d`-tuple of integers. Every combination
    must appear exactly once.
- `∂...;`
  - `∂` is to `D` as `ƒ` is to `F`.
- `I...;`
  - Pop a value and execute the code if the value is truthy.
- `O...;`
  - Pop a value and execute the code if the value is falsey.
- `Í...;`
  - Like `I`, but read the value without popping it.
- `Ó...;`
  - Like `O`, but read the value without popping it.
- `B`
  - Break from the current loop.
- `C`
  - Continue to the next iteration of the current loop.
- `Ç`
  - Terminate the program.
- `ç`
  - Pop a value and break if the value on top of the stack is truthy.
- `ɓ`
  - Break if the top two stack values are equal.
