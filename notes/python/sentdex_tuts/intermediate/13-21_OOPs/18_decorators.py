# Decorators

'''
' Decorators are a way of wrapping a function inside another function,
' without actually hard-coding it to be like this every time.
'''

from functools import wraps


def add_wrapping(item):
    @wraps(item) # fixes the __name__ issue, that is if you want to fix it
    def wrapped_item():
        return "a wrapped up box of {}".format(str(item()))
    return wrapped_item

def add_wrapping_with_style(style):
    def add_wrapping(item):
        def wrapped_item():
            return "a {} wrapped up box of {}".format(style,str(item()))
        return wrapped_item
    return add_wrapping


@add_wrapping_with_style("horribly")
@add_wrapping_with_style("beautifully")
def new_gpu():
    return "a new Tesla P100 GPU"

@add_wrapping
@add_wrapping
def new_bicycle():
    return "a new bicycle"

print(new_gpu())
print(new_bicycle())

print(new_gpu.__name__) # wrapped_item
print(new_bicycle.__name__) # new_bicycle
'''
' we might want the actual name new_gpu
' this can be fixed with "functools import wraps" @wraps(item)
' this is not an issue, it depends on the use case and if the value of __name__
' matters to the program
'''
