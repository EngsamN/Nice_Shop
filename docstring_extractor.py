import os
import sys

def extract_docstrings(directory):
    """Extract docstrings from Python files in the given directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    source_code = f.read()
                docstring = extract_docstring(source_code)
                print(f"Docstring for {filepath}: {docstring}")

def extract_docstring(source_code):
    """Extract the docstring from a Python source code string."""
    # Logic to extract docstring goes here
    pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python docstring_extractor.py <directory>")
        sys.exit(1)
    directory = sys.argv[1]
    extract_docstrings(directory)
