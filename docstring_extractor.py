import os
import sys

def extract_docstrings(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    in_docstring = False
                    docstring_lines = []
                    for line in f:
                        if '"""' in line:
                            if in_docstring:
                                docstring = ''.join(docstring_lines).strip()
                                print(f"Docstring for {filepath}: {docstring}")
                                break
                            else:
                                in_docstring = True
                                docstring_lines.append(line)
                        elif in_docstring:
                            docstring_lines.append(line)
                            if '"""' in line:
                                docstring = ''.join(docstring_lines).strip()
                                print(f"Docstring for {filepath}: {docstring}")
                                break

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python /home/samaih/Django_Shop/docstring_extractor.py /home/samaih/Django_Shop/LabProject")
        sys.exit(1)

    directory = sys.argv[1]
    extract_docstrings(directory)
