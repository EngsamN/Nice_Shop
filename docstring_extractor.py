import os
import sys
import inspect

def extract_docstrings(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        if '"""' in line:
                            start_index = lines.index(line)
                            for i in range(start_index + 1, len(lines)):
                                if '"""' in lines[i]:
                                    docstring = ''.join(lines[start_index + 1:i]).strip()
                                    print(f"Docstring for {filepath}: {docstring}")
                                    break

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:  python /home/samaih/Django_Shop/docstring_extractor.py /home/samaih/Django_Shop/LabProject")
        sys.exit(1)

    directory = sys.argv[1]
    extract_docstrings(directory)
