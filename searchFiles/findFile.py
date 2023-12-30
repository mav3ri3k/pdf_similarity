import os

def clean(str):
    pattern = ""
    i = 0;
    for ch in str:
        if i >= 2:
            break
        pattern += ch
        i += 1 

    if (pattern == "./"):
        return str[2:]
    else:
        return str

def find_file(name, startingPath="."):
    """find_path(name of file, starting path for search(default = "."))
       return {name, extension, filepath}
    recursively searches for given file name in given path
    reaise KeyError if file not found
    """
    path = startingPath
    absolutePath = os.path.abspath(path)

    for root, _, f_names in os.walk(path):
        for file in f_names:
            filepath = f"{absolutePath}/{clean(root)}/{file}"
            extension = os.path.splitext('my_file.txt')[1][1:]

            if name == file:
                return {"name": name,
                        "extension":f".{extension}",
                        "filepath":filepath
                        }
    raise KeyError(f"File: {name}, not found in {absolutePath}")

print(find_file("States.h", "."))
find_file("some", ".")
