import checker
import os


class BotoMarkdown():
    """
        a wrapper around a file to build the boto markdown from a python file
    """
    def __init__(self, filename):
        self.fh = open(filename, 'w')

    def build_title(self, filepath):
        self.fh.write("# %s\n" % " ".join(filepath.split("/")[-1].split(".")[0].split("_")))

    def build_description(self, filepath):
        lines = []
        for line in checker.get_description(file):
            lines.append(line.lstrip('# '))
        self.fh.write("\n".join(lines))

    def build_code_example(self, filepath):
        description_lines = checker.get_description(file)
        with open(filepath, 'rb') as lines:
            code = [line.rstrip("\n") for line in lines if line.rstrip('\n') not in description_lines]
            code.insert(0, "\n```python")
            code.append("```")
            self.fh.write("\n".join(code))


if __name__ == "__main__":
    folders = (os.path.abspath(name) for name in os.listdir(".") if os.path.isdir(name))
    for folder in folders:
        for file in checker.walk_tree(folder):
            print "processing %s" % file
            markdown_filename = "%s.md" % file.rstrip(".py")
            md_file = open(markdown_filename, 'w')
            b = BotoMarkdown(markdown_filename)
            b.build_title(file)
            b.build_description(file)
            b.build_code_example(file)
