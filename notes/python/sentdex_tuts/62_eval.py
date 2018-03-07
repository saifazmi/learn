# Using Eval()

'''
' eval is short for evaluate and is a built-in function
' It evaluates any expression passed through it in form of a string and will
' return the value.
' Keep in mind, just like the pickle module we talked about, eval has
' no security against malicious attacks. Don't use eval if you cannot
' trust the source. For example, some people have considered using eval
' to evaluate strings in the browser from users on their website, as a
' way to create a sort of "online editor." While you can do this, you have
' to be incredibly careful!
'''

# a list as a string
list_str = "[5,6,2,1,2]"
print("BEFORE eval()")
print("list_str", list_str)
print("list_str[2]:", list_str[2])

list_str = eval(list_str)
print("\nAFTER eval()")
print("list_str", list_str)
print("list_str[2]:", list_str[2])

x = input("code:")
print(x)

check_this_out = eval(input("code>"))
print(check_this_out)
