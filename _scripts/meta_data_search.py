import re
import os
import os.path

from read_files import read_file

def _meta_data_search(file_path, memo):
    """
    Extracts meta data from a file and returns it as a dictionary.
    
    The function searches for metadata keywords such as 'Producer:', 'Topics:', 'Type:', and 'Reference:' in the 
    given file. Extracted metadata is added to a memo dictionary.

    Parameters
    ----------
    - file_path (str): The path to the file from which metadata should be extracted.
    - memo (dict): The memoization dictionary used to store metadata information. It is updated in-place.

    Returns:
    - dict: The updated memo dictionary containing metadata for the given file and potentially other files.
    
    Structure of the memo dictionary:
    {
        'filename': {
            'producer': [list of producers],
            'topics': [list of topics],
            'type': [list of types],
            'reference': [list of references]
        },
        ...
    }

    Tip:
    - The function utilizes memoization to avoid redundant parsing of files.
    """
    
    file_name = os.path.basename(file_path)
    file_name, postfix = os.path.splitext(file_name)
        
    # base case to avoid redundant parsing
    if file_name in memo:
        return
    
    memo[file_name] = {}
    file_string = read_file(file_path)

    # Define helper function to reduce code repetition
    def extract_meta_data(regex_pattern, key):
        matches = re.findall(regex_pattern, file_string)
        if matches:
            values = [v.strip() for v in matches[0].split(",")]
            for value in values:
                if value.startswith("[[") and value.endswith("]]"):
                    extracted_string = value[2:-2]
                    memo[file_name][key].append(extracted_string)
                elif value.startswith("#"):
                    extracted_string = value[1:]
                    memo[file_name]['type'].append(extracted_string)
                else:
                    memo[file_name][key].append(value)
    
    # Extract metadata for each category
    for key, pattern in [('producer', r"(?<=Producer:).*"), 
                         ('type', r"(?<=Type:).*"), 
                         ('topic', r"(?<=Topics:).*"), 
                         ('reference', r"(?<=Reference:).*")]:
        memo[file_name][key] = []
        extract_meta_data(pattern, key)
    
    return memo
