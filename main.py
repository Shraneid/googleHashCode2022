from pathlib import Path
import parserInputFiles

def optimize_projects():
    file_path = "./a_an_example.in.txt"
    with open(file_path) as f:
        contributors, projects = parserInputFiles.parse(f.readlines())


if __name__ == '__main__':
    optimize_projects()
