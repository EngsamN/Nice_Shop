#!/bin/bash

# Navigate to the source directory
cd "$(dirname "$0")/source"

# Build the Sphinx documentation
make html

# Check if the build was successful
if [ $? -eq 0 ]; then
    echo "Documentation built successfully."
else
    echo "Documentation build failed."
    exit 1
fi
