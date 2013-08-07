"""
A script to build up a markdown file from python source code
"""

import checker
import os
import re


class BotoMarkdownBuilder():
    """
        a wrapper around a file to build the boto markdown from a python file
    """
    def __init__(self, filename):
        self.filename = filename
        self.code = ""
        self.title = ""
        self.description = ""

    def add_title(self, filepath):
        self.title = "# %s\n" % " ".join(filepath.split("/")[-1].split(".")[0].split("_"))

    def add_description(self, filepath):
        lines = []
        for line in checker.get_description(file):
            lines.append(line.lstrip('# '))
        self.description = "\n".join(lines)

    def add_code_example(self, filepath):
        description_lines = checker.get_description(file)
        with open(filepath, 'rb') as lines:
            code = [line.rstrip("\n") for line in lines if line.rstrip('\n') not in description_lines and not re.match("#\s[d|D]escription", line)]
            code.insert(0, "\n```python")
            code.append("```")
            self.code =  "\n".join(code)

    def build(self):
        fh = open(self.filename, 'w')
        fh.write("\n".join([self.title, self.description, self.code]))
        fh.close()


if __name__ == "__main__":
    folders = (os.path.abspath(name) for name in os.listdir(".") if os.path.isdir(name))
    for folder in folders:
        for file in checker.walk_tree(folder):
            print "processing %s" % file
            markdown_filename = "%s.md" % file.rstrip(".py")
            md_file = open(markdown_filename, 'w')
            b = BotoMarkdownBuilder(markdown_filename)
            b.add_title(file)
            b.add_description(file)
            b.add_code_example(file)
            b.build()
