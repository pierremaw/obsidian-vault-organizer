import os
import fnmatch

def read_file(file_path):
    """
    Reads the content of a file.
    
    This function tries to read a file using 'utf-8' encoding. If it encounters a UnicodeDecodeError,
    it attempts to read the file again using the 'ISO-8859-1' encoding.
    
    Parameters
    ----------
    - file_path (str): The path to the file to be read.
    
    Returns
    -------
    - str: The content of the file.
    
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            file_contents = f.read()
        return file_contents
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='ISO-8859-1') as f:
            file_contents = f.read()
        return file_contents

def read_file_lines(file_path):
    """
    Reads the lines of a file.
    
    This function reads a file and returns its content as a list of lines.
    
    Parameters
    ----------
    - file_path (str): The path to the file to be read.
    
    Returns
    -------
    - list of str: A list containing each line of the file as a separate string.
    """
    with open(file_path, "r") as f:
        file_contents = f.readlines()
    return file_contents
