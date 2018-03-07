# URLLIB module

'''
' Allows us to access the internet via python
'''

# Python2 we can import simply urllib or urllib2
# This is because now urllib is a folder which contains respective modules
import urllib.request
import urllib.parse # helps parse values to POST request

# make a GET (default) request object to the URL
x = urllib.request.urlopen("https://www.google.com")

print(x.read()) # source code of the requested webpage

# make a POST request
url = "https://pythonprogramming.net/search"
values = {'q':"basic"}

# urlencode() will encode it as it should be in the URL 
data = urllib.parse.urlencode(values)
data = data.encode("utf-8") # puts the data in bytes using the encoding format

# Build POST request url with the variables
req = urllib.request.Request(url, data)

# Get response of the request
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)

'''
' People/Companies don't like it when someone visits their website with a bot
' program like this one, so they generally have filters in place to detect a
' bot, for example, following code will return HTTP Error 403: Forbidden
'''

try:
    g = urllib.request.urlopen("https://www.google.com/search?q=test")

    print(g.read())
    
except Exception as e:
    print(str(e))

'''
' The above piece of code is pretty easy for web servers to detect as a bot
' because of the "User-Agent" parameter in the header of the request.
' This parameter defines the type of browser that the user is using.
'
' By default urlopen() defines the User-Agent in the header as
' "Python-urllib/<python_version> which is fairly easy to detect and filter out
'
' We can get around this by faking our User-Agent as a legitimet browser
'''

try:
    url = "https://www.google.com/search?q=test"

    headers = {}
    headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    
    # Since there is a lot of data on the results page lets write it out
    saveFile = open("withHeaders.txt", 'w')
    saveFile.write(str(respData))
    saveFile.close()

except Exception as e:
    print(str(e))
