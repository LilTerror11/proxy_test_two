import os
from typing import Any
from builtins import print as log

Assets = {}

f = open("out.txt", "w")


def print(msg: Any = "", end="\n"):
    log(msg, end=end)
    f.write(msg + end)


def scan_dir(directory: str, loops=0):
    scanned = os.scandir(directory)
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
            print("  "*loops + "\"" + path.name + "\"", end="")
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


scan_dir("./..")
