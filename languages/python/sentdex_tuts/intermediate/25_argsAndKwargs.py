# Args and Kwargs

'''
' The idea behind *args and **kwargs is that there may be times when you
' have a function and you want to be able to handle an unknown number of
' arguments. The *args will handle for any number of parameters, and **kwargs
' will handle for any number of keyword arguments (hence kwargs)
'
' One can think of *args as a list and **kwargs as a dictionary
'''

blog_1 = "I am so awesome."
blog_2 = "Cars are cool."
blog_3 = "Aww look at my cat!!"


site_title = "My Blog"

## *args parameters
def blog_posts(title, *args):
    print(title)
    for post in args:
        print(post)

print("#### ARGS ####")
blog_posts(blog_1) # pass one argument
blog_posts(blog_1, blog_2, blog_3) # or more than one
blog_posts(site_title, blog_1, blog_2, blog_3) # can also pass specific parameter


## **kwargs parameters
def blog_posts(title, **kwargs):
    print(title)
    for p_title, post in kwargs.items():
        print(p_title, post)

print("#### KWARGS ####")
blog_posts(site_title,
           blog_1 = "I am so awesome.",
           blog_2 = "Cars are cool.",
           blog_3 = "Aww look at my cat!!")

## *args AND **kwargs parameters
def blog_posts(title, *args, **kwargs):
    print(title)
    for arg in args:
        print(arg)
    for p_title, post in kwargs.items():
        print(p_title, post)

print("#### ARGS and KWARGS ####")
blog_posts(site_title,
           '1', '2', '3',
           blog_1 = "I am so awesome.",
           blog_2 = "Cars are cool.",
           blog_3 = "Aww look at my cat!!")


# Another way of using *args
import matplotlib.pyplot as plt

def graph_operation(x, y):
    print("function that graphs {} and {}".format(str(x), str(y)))
    plt.plot(x,y)
    plt.show()

x1 = [1, 2, 3]
y1 = [2, 3, 1]

graph_me = [x1, y1]

graph_operation(*graph_me)
