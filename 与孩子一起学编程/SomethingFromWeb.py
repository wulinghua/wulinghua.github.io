import urllib
file=urllib.urlopen('http://hellpworldbook.com/data/message.txt')
message=file.read()
print message
