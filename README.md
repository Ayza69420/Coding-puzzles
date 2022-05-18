# Coding-puzzles

This was inspired by codingame puzzles. Done this quickly for fun, the code may look bad.

Run the ``main.py`` first, to get the puzzle and follow the instructions given.

You enter your solution in the ``Executor.py`` file, there must be a function called "solution" and takes one argument which is the input, once done, return the result.

You could add puzzles through the ``puzzles.json`` file, create a dictionary that contains 3 keys: name, statement and testcases. The testcases is a 2D array where each array is a seperate testcase, each array contains an input and output where the first value is the input and the second is the expected output will be used to test the solution and determine the score (didn't add validators here, because they are unnecessary), the name will be used as an identifier to the puzzle if the user wants to pick the puzzle manually, the statement will be used as the instructions to the puzzle, and the constraints are to describe the variables constraints.

**Required modules:** ``colorama``
