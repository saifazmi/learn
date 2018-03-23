# Basics

### Launching Python

#### Interpreter (interactive shell)
```bash
# python 2
$ python
```

```bash
# python 3
$ python3
```

#### IDLE
```bash
$ idle3
```

#### Python prompt
```python
>>>
```

### Hello World
A simple `print` statement.

```python
>>> print("Hello, world")
```

### File extensions
- .py: This is normally the input source code that you've written.
- .pyc: This is the compiled bytecode. If you import a module, python will build a *.pyc file that contains the bytecode to make importing it again later easier (and faster).
- .pyo: This is a *.pyc file that was created while optimizations (-O) was on.
- .pyd: This is basically a windows dll file. http://docs.python.org/faq/windows.html#is-a-pyd-file-the-same-as-a-dll

> http://stackoverflow.com/questions/8822335/what-do-the-python-file-extensions-pyc-pyd-pyo-stand-for

### Basic Errors

#### EOL Error
_End of Line_ is a **syntax error**
`EOL while scanning string literal`
This happens when Python got all the way to the end of the line and never found the end of your string of text.

#### NameError
_NameError_ is a **runtime error**
`NameError: name 'Hello' is not defined`
This happens when we are referencing a variable but Python cannot find the definition of the variable.

### Comments
Python uses `#` for single line comments and for multi-line comments use `"""` or `'''`

**Example**
```python
# This is a single line comment

"""
Multi-line comment
I have a lot to say, hmm...
"""

'''
Blah blah blah
bla bla blah
'''
```

### Variables
Python variables are case sensitive