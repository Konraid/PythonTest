#################################################
#                                               #
#           made by Konrad Brandts              #
#                                               #
#               Version 1.0                     #
#                                               #
#################################################

import os

def __getUID__(name):
    import urllib.request
    request = urllib.request.urlopen('https://api.mojang.com/users/profiles/minecraft/' + name)
    content = request.read()
    request.close()
    string = content.decode("utf-8")

    return string[7:39]

def __writeVaroFile__():
    name = None
    name = input("Namen eingeben:\n")
    uid = __getUID__(name)
    f = open('varo.yml', 'a')
    f.write("\n  " + uid + ":")
    f.write("\n    Name: " + name)
    f.write("\n    Team:")
    f.write("\n    Time: 7200")
    f.write("\n    Location: #BENÖTIGE INFOS VON LUCA")
    f.close()
    print("Wurde erfolgreich gespeichert!")


def __init__():
    print("Das Programm wird gestartet....")
    __writeVaroFile__()

__init__()

while True:
    inputText = None
    inputText = input("Möchten Sie einen weiteren Namen eingeben?" + os.linesep)
    if inputText.lower() == "ja":
        __writeVaroFile__()
    elif inputText.lower() == "nein":
        break
    else:
        continue

print("Das Programm wird beendet!")