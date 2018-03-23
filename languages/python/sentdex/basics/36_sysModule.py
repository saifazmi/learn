# SYS module

import sys

# stderr: write to the standard error buffer
sys.stderr.write("This is stderr text\n") # red error text
sys.stderr.flush() # good idea to flush after writing to stderr

# stdout: write to the standard output buffer
sys.stdout.write("This is stdout text\n")

# argv
print(sys.argv) # print the full path of the current file
'''
' This lets us to pass parameters to this file via commandline,
' essentially acting as a bridge between python and other languages
' sys.argv will display ALL the arguments as argv is a essentially a list
' of arguments, by default the first argument is the script/file name
'
' When accepting arguments from commandline, its a good idea to check
' if they are passed in the first place before we start using them
'''

if len(sys.argv) > 1:
    print(sys.argv[1])
    print(float(sys.argv[1])+5) # manipulating commandline arguments

# Example of communicating with other programs by using argv as param for func
def main(arg):
    print(arg)

main(sys.argv[1])    
