import checker
import os


class BotoMarkdown():
    """
        a wrapper around a file to build the boto markdown from a python file
    """
    def __init__(self, filename):
        self.fh = open(filename, 'w')

    def build_description(self, filepath):
        lines = []
        for line in checker.get_description(file):
            lines.append(line.lstrip('# '))
        self.fh.write("\n".join(lines))

    def build_code_example(self, filepath):
        return None


if __name__ == "__main__":
    folders = (os.path.abspath(name) for name in os.listdir(".") if os.path.isdir(name))
    for folder in folders:
        for file in checker.walk_tree(folder):
            print "processing %s" % file
            markdown_filename = "%s.md" % file.rstrip(".py")
            md_file = open(markdown_filename, 'w')
            b = BotoMarkdown(markdown_filename)
            b.build_description(file)
            b.build_code_example(file)
