# Subprocess Module

'''
' The subprocess module lets us communicate with the commandline and
' run commands there.
'
' This command is best seen in the interpreter:
' >>> import subprocess
' >>> subprocess.call("ls", shell=True)
' backups  Documents  Downloads  learn
' Desktop  dotfiles   Pictures
' 0
'
' if we try to print the output for this command, it just results in getting 0
' To use this in a script, we can use the check_output() function
'''

import subprocess

# This gives us a string which contains newlines and can be split based on that
output = subprocess.check_output("ls", shell=True)
print(output)
      
# This also enables us to communicate between scripts and modules
'''
' >>> subprocess.call('python 36_sysModule.py 5', shell=True)
' This is stderr text
' This is stdout text
' ['36_sysModule.py', '5']
' 5
' 10.0
' 5
' 0
'''

output = subprocess.check_output('python 36_sysModule.py 5', shell=True)
print(output)
