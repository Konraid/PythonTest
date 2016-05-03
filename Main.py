import os

def __getUID__(name):
    import urllib.request
    request = urllib.request.urlopen('https://api.mojang.com/users/profiles/minecraft/' + name)
    content = request.read()

    string = content.decode("utf-8")

    return string[7:39]

def __userInput__():
    name = input("Namen eingeben:\n")
    uid = __getUID__(name)
    return uid

def __init__():
    print("Das Programm wird gestartet....")
    __userInput__()

#__init__()



print("Das Programm wird beendet!")
f = open('varo.yml', 'w')
f.write("")
f.close()