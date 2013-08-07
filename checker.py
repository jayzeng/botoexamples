import os
import re

def walk_tree(folder_name):
    """
    Retrieve all python files
    """
    for path, diralist, filelist in os.walk(folder_name):
        return (path + '/' + py_file for py_file in filelist if py_file.endswith('.py'))

def get_description(folder):
    desc_regex = re.compile('#\s[D\d]escription:(\n(.*))\n')

    for file in walk_tree(folder):
        with open(file, 'rb') as python_reader:
            contents = python_reader.read(50000)

            match = desc_regex.search(contents)

            if not match:
                raise SyntaxError(" # Description")
            print match.group(0).splitlines()[1:]

if __name__ == "__main__":
    folders = (os.path.abspath(name) for name in os.listdir(".") if os.path.isdir(name))
    for folder in folders:
        print get_description(folder)
