import os

path = {}


def scan_dir(directory: str, log: bool = False):
    scanned = os.scandir(directory)
    for path in scanned:
        path: os.DirEntry
        if path.is_dir():
            try:
                dict_path = str(f"{directory}/{path.name}").split("/")
                dict_path = '/'.join(dict_path)
                dict_path = dict_path.replace("/", "\"][\"")
                exec("Assets[\"" + dict_path + "\"] = {}")
            except Exception as e:
                pass
            scan_dir(f"{directory}/{path.name}")
        elif path.is_file():
            if log:
                print(f"{directory}/{path.name}")
            dict_path = str(f"{directory}/{path.name}").split("/")
            dict_path = dict_path.replace("/", "\"][\"")
            exec(f"path[\"{dict_path}\"] = image")
        else:
            if log:
                print("IDK what this is")
                print(path.stat())
            pass


scan_dir("/")