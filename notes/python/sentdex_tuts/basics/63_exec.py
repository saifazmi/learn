# Using Exec

'''
' exec() is a built-in function and is perhaps the most dangerous yet cool
' thing, as it is step-up from eval() since it compiles and evaluates
' whatever is passed through in string form; essentially acting as a compiler
' inside a compiler. So be very carefull on web-server, virual machines, etc.
'''

exec("print('so this works like eval')")

list_str = "[5,6,2,1,2]"
list_str = exec(list_str) # None, because this is the action of defining a list
print(list_str)

exec("list_str2 = [5,6,2,1,2]") # defines and assigns i.e. execution over eval
print(list_str2) # will print the list

# defining functions
exec("def test(): print('hot diggity')")
test()

exec("""
def test2():
    print('testing to see if multiple lines work...')
""")
test2()
