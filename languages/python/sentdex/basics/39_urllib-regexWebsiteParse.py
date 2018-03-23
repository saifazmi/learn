# Parsing a Website using urllib and regex (re)

import urllib.request
import urllib.parse
import re


url = "https://pythonprogramming.net/search"
values = {'q':"basic"}

data = urllib.parse.urlencode(values)
data = data.encode("utf-8")
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

# print(respData)

'''
' Find everything between <p> tags
' The period says find any character except a newline and the * modifies it
' to say that it should be done 1 or more times and the final ? defines
' that this combination of .* should take place 0 or 1 times.
'''
paragraphs = re.findall(r"<p>(.*?)</p>", str(respData))

for eachP in paragraphs:
    print(eachP)
