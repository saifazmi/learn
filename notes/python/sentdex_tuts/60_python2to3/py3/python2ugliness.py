# Converting python 2 to 3

import urllib.request, urllib.error, urllib.parse

try:
    x = urllib.request.urlopen("http://pythonprogramming.net").read()
    print(x)
    
except Exception as e:
    print(str(e))


'''
' Use the following command to converting any script from py2 to py3
' $ 2to3 <python2_script.py>
'
' RefactoringTool: Skipping optional fixer: buffer
' RefactoringTool: Skipping optional fixer: idioms
' RefactoringTool: Skipping optional fixer: set_literal
' RefactoringTool: Skipping optional fixer: ws_comma
' RefactoringTool: Refactored python2ugliness.py
' --- python2ugliness.py	(original)
' +++ python2ugliness.py	(refactored)
' @@ -1,13 +1,13 @@
' # Converting python 2 to 3
' 
' -import urllib2
' +import urllib.request, urllib.error, urllib.parse
 
'  try:
' -    x = urllib2.urlopen("http://pythonprogramming.net").read()
' -    print x
' +    x = urllib.request.urlopen("http://pythonprogramming.net").read()
' +    print(x)
'      
' -except Exception, e:
' -    print str(e)
' +except Exception as e:
' +    print(str(e))
'   
' RefactoringTool: Files that need to be modified:
' RefactoringTool: python2ugliness.py
'''

'''
' The above command will only show the message and will not actually change
' the file, we can use the following command to change the file
'
' $ 2to3 -w <python2_script.py>
' This creates a *.bak file of the original script and modifies the source
'
' We can create a new directory and put our py3 script there without changing
' the original and creating a backup of the original using the following
'
' $ 2to3 -wn <python2_script.py> -o ./py3script
'''
