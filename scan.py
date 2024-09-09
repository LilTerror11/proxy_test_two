import os
from typing import Any
from builtins import print as log

length = int(open("len.txt", 'r').read().replace("\n", ""))

paths = "."

Assets = {}

f = open("out.txt", "w")

out = ""

#def print(msg: Any = "", end="\n"):
#    global out
#    out = out + msg + end


#def print(msg: Any = "", end="\n"):
#    log(msg, end=end)
#    f.write(msg + end)


def scan_dir(directory: str, loops=0):
    try:
        scanned = os.scandir(directory)
    except:
        print(f"Unable to open path: {directory}")
        return
    help_me = []
    scanny = scanned
    for x in scanny:
        #print(x)
        help_me.append(x)
    #print(help_me)

    #print(scanned)

    for path in help_me:
        i = help_me.index(path) + 1
        path: os.DirEntry
        if path.is_dir():
            try:
                print("  "*loops + "\"" + path.name + "\": {")
                dict_path = str(f"{directory}/{path.name}")
                dict_path = dict_path.replace("/", "\"][\"")
                #exec("Assets[\"" + dict_path + "\"] = {}")
            except Exception as e:
                print(e)
            scan_dir(f"{directory}/{path.name}", loops+1)
            print("  "*loops + "}", end="")
            #if loops != 0:
            #    print(",", end="")
            #   print()
        elif path.is_file():
            #dat = open(path.path, "r").read()
            print("  "*loops + "\"" + path.name, end="")# + "\": " + dat, end="")
            #print(f"{directory}/{path.name}")
            dict_path = str(f"{directory}/{path.name}")
            dict_path = dict_path.replace("/", "\"][\"")
            #value = path.name
            #exec(f"Assets[\"{dict_path}\"] = value")
        else:
            print("IDK what this is")
            print(path.stat())
            pass
        if i != len(help_me):
            print(",", end="")
        print()

ran = False

for i in range(length):
    try:
        os.scandir(paths + "/..")
        paths = paths + "/.."
    except:
        scan_dir(path)
        ran = True
        break
if not ran:
    scan_dir(paths)
#print(open("out.txt", "r").read())
#print(out)
