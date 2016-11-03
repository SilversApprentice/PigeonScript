# Instruction Listings #

## Instructions ##

- `[a-f]` (0 inputs)
  - Push the value of the variable onto the stack: `12` -> `12,6`
- `[value][A-F]` (1 input)
  - Store the value in that variable: `12A` -> `a`
- `+` (2 inputs)
  - *int, int*: Adds two integers: `1,1` -> `2`
  - *array, array*: Concantenates two arrays: `[1,2,3],[4,5,6]` -> `[1,2,3,4,5,6]`
  - *ASCII-art, ASCII-art*: Horizontally concatenates two ASCII-arts: `{"ab","cd"},{"12","34"}` -> `{"ab12","cd34"}`
- `-` (2 inputs)
  - *int, int*: Subtracts two integers: `3,1` -> `2`.
  - *array, **: Appends into the array: `[1,2],3` -> `[1,2,3]`
  - *ASCII-art, ASCII-art*: Vertically concatenates two ASCII-arts: `{"ab","cd"},{"12","34"}` -> `{"ab", "cd", "12", "34"}`
- `n` (0 inputs)
  - Input an integer and push it onto the stack: `1,2` -> `1,2,3`
- `N` (0 inputs)
  - Input a list of integers: `1,2` -> `1,2,[3,4,5]`
- `m` (0 inputs)
  - Input a one-line ASCII art (a string): `{"spam","eggs"}` -> `{"spam","eggs"},{"foo"}`
- `A` (0 inputs)
  - Input an ASCII-art: `1,2,3` -> `1,2,3,{"spam","eggs"}`
- `M` (0 inputs)
  - If the `M` command has not been run before, input an integer and push it onto the stack. Otherwise, push the input
    onto the stack: `1,2,3` -> `1,2,3,4` -> `1,2,3,4,4`
- `s` (0 inputs)
  - Read a string and push an array containing the ASCII-values of all the characters onto the stack: `1,2` -> `1,2,104,101,108,108,111`
- `|` (0 inputs)
  - Skip to the next newline (used for comments).
- `S` (1 input)
  - *int*: Square the integer: `3` -> `9`
  - *array*: Apply the `S` operator to every element in the array: `[1,2,3,4]` -> `[1,4,9,16]`
  - *ASCII-art*: Rotate the ASCII-art: `{"foo","bar","baz"}` -> `{"fbb","oaa","orz"}`
- `C` (1 input)
  - *int*: Cube the integer: `3` -> `27`
  - *array*: Apply the `C` operator to every element in the array: `[1,2,[3,2]]` -> `[1,8,[27,8]]`
- `E` (1 input)
  - *int*: Yield an array with the numbers from 0 to n-1: `4` -> `[1,2,3,4]`
  - *array*: Sum the array: `[1,2,3]` -> `6` 
  - *ASCII-art*: Convert the ASCII art into an array of arrays containing the ASCII-values of each character: `{"foo","bar"}` -> `[[102,111,111],[98,97,114]]`
- `%` (2 inputs)
  - *int, int*: Return (the bigger value) mod (the smaller value)
- `!` (1 input)
  - *int*: Return the factorial of the integer: `3!` -> `6`
- `:` (1 input)
  - Duplicate the value on top of the stack: `[1,2,3]` -> `[2,2,3]`
  
## Control Structures ##

- `w...;`
  - While the top element on the stack has a truthy value (number > 1, non-empty list/ASCII art)
- `u...;`
  - Until the top element on the stack has a truthy value
- `F[name]...;` (`[name]` is a variable name)
  - Take a value `t` from the top of the stack. If `t` is an int, this is equivalent to `for (var [name] = 1;
    n < t; n++) {...}`. If `t` is an array, this is equivalent to `foreach (t as [name]) {...}`.
- `g...;`
  - Like `F`, but automatically uses the variable `e` for `[name]`. If `e` is already used, keep going
    alphabetically until it finds an unused character. (`e`,`f`,`aa`,`ab`...`ff`,`aaa`)
- `D[name]...;` (`[name]` is a variable name)
  - Pop a value `d`. `[name]` will loop through every possible value for a `d`-tuple of integers. Every combination
    must appear exactly once.
- `G...;`
  - `G` is to `D` as `g` is to `F`.
- `i...;`
  - Pop a value and execute the code if the value is truthy.
- `U...;`
  - Pop a value and execute the code if the value is falsey.
- `I...;`
  - Like `i`, but read the value without popping it.
- `O...;`
  - Like `o`, but read the value without popping it.
- `B`
  - Break from the current loop.
- `C`
  - Continue to the next iteration of the current loop.
- `t`
  - Terminate the program.
- `h`
  - Pop a value and break if the value on top of the stack is truthy.
- `r`
  - Break if the top two stack values are equal.
