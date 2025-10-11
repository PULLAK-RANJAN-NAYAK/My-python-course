# PYTHON PROGRAM TO PRINT THE CONTENTS OF THE DIRECTORY USING THE OS MUDULE

import os

# Specify the directory you want to list
directory = "/New folder"  # "." means current directory, or put a path like "C:/Users/Ranjan/Documents"

# List all files and directories
contents = os.listdir(directory)

print(f"Contents of the directory '{directory}':\n")
for item in contents:
    print(item)
