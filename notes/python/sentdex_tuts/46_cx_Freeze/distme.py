# CX_Freeze module

'''
' cx_freeze is not a standard library module, it lets us create an exe file
' from a python module, this is quite handy when trying to distribute our code
'
' To test this lets use some earlier code for example the following parser
'''

import urllib.request
import urllib.parse
import re
import time


url = 'http://pythonprogramming.net'
values = {'s' : 'basics',
          'submit' : 'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

for eachParagraph in paragraphs:
    print(eachParagraph)

time.sleep(15)

'''
' Now we need to create another python file "setup.py" that file is needed
' for cx_freeze to work
'''
