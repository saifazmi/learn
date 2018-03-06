# Strings and Methods

## Declaring Strings

Storing string literals in `string` variables.

```python
phrase = 'Hello, world.'
my_string = "We're #1!"
string_number = "1234"
conversation = 'I said, "Put it over by the llama."'
```

In the second and the last string, we didn't have any trouble using quotation marks, as based on the situation we used different quotations to define the string literal. There are other ways to get around this issue, but it's worth highlighting that python provides this flexibility.

We can also have multi-line strings, which respect the newline formatting.

```python
long_string = """This is a multi-
line string. It will print in two lines"""

long_string_2 = '''We can also use the apostrophes
for multi-line string, just like multi-line comments
    and also preserve white spaces.'''
```

> **Pro-tip**
> If you want to write a long string on multiple lines in your program but don't want to print it in the same way i.e. on multiple lines you can use a backslash.
>
> ```python
> long_string = "This is gonna be a long string but I don't mind \
> because I know this neat backslash trick."
> ```

## Common string operations

### String length: `len()`

```python
>>> print(len("abc"))
3
```

### String concatenation: `+`

```python
>>> print("abc" + "def")
abcdef
```

Another way to print out multiple string literals as one is by using commas `,` in the print statement. This will automatically add spaces between them.
```python
>>> print("abc", "xyz")
abc xyz 
```

### Selecting each `char` in a string

Characters in a string can be accessed just like an array, since string literals are technically `char[]`. And of course it start from `0`

```python
>>> spell = "black lotus"
>>> print(spell[6])
l
```

The way we're using brackets after the string is referred to as subscripting or indexing since it uses the index numbers of the string's characters.

> **NOTE:** for the sake of simplicity I say that a string is a `char[]` i.e. character array but technically in python it's **NOT** an array, as python doesn't implement collections as array internally.
> 
> The default built-in Python type is a list, and not an array. It is an ordered container of arbitrary length that can hold a heterogeneous collection of objects (their types do not matter and can be freely mixed). This should not be confused with the `array` module, which offers a type closer to the C array type; the contents must be homogeneous (all of the same type), but the length is still dynamic.
> 
> _http://stackoverflow.com/questions/1514553/how-to-declare-an-array-in-python_

### Selecting a particular section in a string

This can be done by defining a range of index values separated by a colon `:`

```python
>>> spell = "black lotus"
>>> print(spell[0:3])
bla
```

Here we are telling Python to print only the first three characters of our string, starting from the 0th character till (but **not** including) the 3rd character.

We can also omit one or both of the numbers in the range definition.

```python
>>> spell = "black lotus"
>>> print(spell[:5]) # no starting bounds
black
>>> print(spell[5:]) # no ending bounds
 lotus
>>> print(spell[:]) # no bounds
black lotus
```

> **NOTE:** When no bounds are defined Python goes all the way in that direction

### Python strings are _immutable_

Python strings are immutable, meaning that they can't be changed once you've created them. For instance, see what happens when you try to assign a new letter to one particular character of a string:

```python
>>> my_string = "goal" 
>>> my_string[0] = "f" # this won't work!
```

Instead, we would have to create an entirely new string (although we can still give `my_string` that new value): 

```python
>>> my_string = "goal" 
>>> my_string = "f" + my_string[1:] 
```

In the first example, we were trying to change part of `my_string` and keep the rest of it unchanged, which doesn't work. In the second example, we created a new string by adding two strings together, one of which was a part of `my_string`; then we took that new string and completely reassigned `my_string` to this new value.

## Use Objects and Methods

Python is an example of an Object-Oriented Programming (OOP) language. This means that information is stored in objects. A _string_ is an example of an object in python. Strings are very simple objects, they only hold one piece of information i.e. their value.

But an object can be very complex if needed. It can even hold other objects inside it. This helps to give structure and organisation to the program.

