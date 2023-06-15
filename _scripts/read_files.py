import os
import fnmatch

'''
READ FILE FUNCTION
TASK: Reads a file and returns the contents as a string
'''
def read_file(file_path):
    
    with open(file_path, "r") as f:
        file_contents = f.read()
    return file_contents

'''
READ FILE LINES FUNCTION
TASK: Read a file and return the contents as a list that contains lines
'''
def read_file_lines(file_path):

    with open(file_path, "r") as f:
        file_contents = f.readlines()
    return file_contents
