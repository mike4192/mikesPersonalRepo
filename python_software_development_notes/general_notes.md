# Python Program Development General Notes 

* [Name and Main](#name-and-main)
* [Bash Specification](#bash-specification)



## Name and Main
Sometimes see `if __name__ == __main__` in python code. The purpose is to allow a piece of code to execute either as a standalone script, or be imported as a library and not execute the main function.

#### Example Code

```python
# Suppose this is foo.py.

print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")
```
When python reads a source file, it first defines some special variables, one is `__name__`. When your module is the main program, e.g.
`python foo.py`
the interpreter assings the string `"__main__"` to the `__name__` variable.
\
If your module is imported by another, e.g.:
```python
# Suppose this is in some other main program
import foo
```
then `__name__` gets assigned a string that is the name of the file, in this case `"foo"`.
\
For the example above, if `foo.py` is run itself, functions A and B are executed. If `foo.py` is imported in another program, then functions A and B will not be executed.

#### Uses
* Your module is a library, but you want to have a script mode where it runs some unit tests or a demo.
* Your module is only used as a main program, but it has some unit tests, and the testing framework works by importing .py files like your script and running special test functions. You don't want it to try running the script just because it's importing the module.
* Your module is mostly used as a main program, but it also provides a programmer-friendly API for advanced users.

[See this stackoverflow post for more info.](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)


## Bash Specification
The line `#!/usr/bin/python` is called the 'shebang' and it indicates the path to the interpreter binary that will be used to interpret the rest of the commands in the file. It is usually the first line of a script.

So the line `#!/usr/bin/python` indicates that the content of the file will be interpreted by the python binary located at /usr/bin/python.

Note that the shebang line is parsed by the kernel and then the script will eventually be called as an argument:
`python script_name`

Similarly in case of `#!/bin/bash`:
`bash script_name`