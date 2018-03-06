# ftpLib

'''
' FTP is not really secure and there are much better options like ssh, scp      
' But since its still used, its good to know how to interact with it
'''

from ftplib import FTP

ftp = FTP("domainname.com") # connects to root directory
ftp.login(user="username", passwd="password")

# Change directory
ftp.cwd("/specificdomain-or-location/")

def grabFile():
    filename = "fileName.txt" # name of the file from the server
    localfile = open(filename, 'wb') # local file
    ftp.retrbinary("RETR " + filename, localfile.write, 1024) # retrive file

    ftp.quit
    localfile.close()


def placeFile():
    filename = "fileName.txt"
    ftp.storbinay("STOR " + filename, open(filename, 'rb'))
    ftp.quit()

'''
' Maybe move filename to function parameter
'''
