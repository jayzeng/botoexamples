import checker
import os

if __name__ == "__main__":
    folders = (os.path.abspath(name) for name in os.listdir(".") if os.path.isdir(name))
    for folder in folders:
        for file in checker.walk_tree(folder):
            markdown_filename = "%s.md" % file.rstrip(".py")
            md_file = open(markdown_filename, 'w')
            lines = []
            for line in checker.get_description(file):
                lines.append(line.lstrip('# '))
            md_file.write("\n".join(lines))
