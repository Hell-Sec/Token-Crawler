import requests
import re
import time, random, os, sys, urllib
from urllib.parse import unquote
print (" ░░░░░▒░░░░░░░░▐▌░░░░░░░")
print (" ░░▐░░▓░░░░░░░░▓░░░░▄▄░░")
print (" ░░▐▌░▀▌░░░░░░▄░░▄▒▀▀░░░")
print (" ░░░▀▒░▐▄░▄░▐▐▌░▓▀░░░░░░")
print (" ░░░░░▀▄▐▄▄▄▄▐▌▓░░░░░░░░")
print (" ░░░░░░░▀▐███▓▀░░░░░░░░░")
print (" ░░░░░░░▄▄▐█▓▓▄░░░░░░░░░")
print (" ░░░░░▄▀▀▓▓▓▓▓▀▀▄░░░░░░░")
print (" ░░░▄▀░░▐▌▐█▌▐▌░░▀▒▄░░░░")
print (" ░░░▐░░▐▀░░▀▀░▒░░░░▀░░░░")
print (" ░░░░░▐▌░░░░░░░▒░░░░░░░░")
print (" ░░░░▄▒░░░░░░░░░▀░░░░░░░")
print ("Token Crawler")
print ("")
print ("Created by Lucifer's Angel#3722")
print ("")
print ("Enter A Link To Scan")

link = input("> ")
clear = lambda: os.system('cls')

with open('Links.txt', 'w') as filehandle:
    for listitem in link:
        filehandle.write('%s' % listitem)

ObjRead = open("Links.txt", "r")
 
link = ObjRead.read();

ObjRead.close()

data = requests.get(link)

Token = re.findall(r'([\w-]{24}\.[\w-]{6}\.[\w-]{27})', data.text)

with open('Tokens.txt', 'w') as filehandle:
    for listitem in Token:
        filehandle.write('%s\n' % listitem)

num_tokens = sum(1 for line in open('Tokens.txt'))

print ("--------------------------------------")
print ("Tokens Found -", num_tokens)
print ("Discord Tokens From -", link)
print ("Tokens located in Tokens.txt")
print("--------------------------------------")
input('Press ENTER to exit')
exit
clear()
##https://pastebin.com/f6hdcM3t