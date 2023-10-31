import re
import os
import os.path
from collections import deque

from config import vault_path, producer_folder_name, template_folder_name
from read_files import read_file

def producer_search(file_path: str, memo_file_paths: dict, memo_file_meta_data: dict) -> list:
    """
    Search for and format the unique producers linked to a given file.

    Given a file path, this function identifies and formats the associated producers. 
    It also checks if a note exists for each producer in a specific vault location. If not, it creates one.

    Parameters:
    - file_path (str): The path to the file of interest.
    - memo_file_paths (dict): A dictionary containing file paths indexed by their associated names.
    - memo_file_meta_data (dict): A dictionary containing meta-data associated with file names.

    Returns:
    - list: A list of unique producer names. Returns None if no producers are found or if an exception occurs.

    Notes:
    The function expects certain folder names like 'template_folder_name' and 'producer_folder_name' to be 
    globally defined. Similarly, functions like 'read_file' and global variables like 'vault_path' 
    should be defined elsewhere in the code for this function to work correctly.
    """

    try:
        # Skip processing if the file is in the template folder
        if template_folder_name in file_path:
            return

        # Initialize memoization dictionary and retrieve producers
        memo = {}
        producers = _producer_search(file_path, memo, memo_file_paths, memo_file_meta_data)

        # Return if no producers are found
        if not producers:
            return 

        # Filter out duplicate producers
        unique_producers = []
        queue = deque(producers)
        while queue:
            element = queue.popleft()
            if element not in unique_producers:
                unique_producers.append(element.strip())

        # Return if no valid producers are identified
        if unique_producers == ['']:
            return

        # Format the list of unique producers
        new_producers = [f'[[{producer}]]' for producer in unique_producers]
        new_producer_string = " " + ", ".join(new_producers)

        # Update the original file with the formatted list of producers
        file_string = read_file(f"{file_path}")
        new_file_string = re.sub(r"(?<=Producer:).*", new_producer_string, file_string)

        # Write the updated content back to the file
        with open(file_path, "w") as f:
            f.write(new_file_string)

        # For each producer, check if there exists a note in the vault; if not, create one
        for producer in unique_producers:
            if producer not in memo_file_paths.keys():
                new_file_path = os.path.join(f'{vault_path}', producer_folder_name, f'{producer}.md')
                with open(new_file_path, "w") as f:
                    f.write(f'Type: #producer\n')
                    f.write(f'___\n')

    except:
        # Silently handle exceptions and return
        return

    return unique_producers


def _producer_search(file_path, memo, memo_file_path, memo_file_meta_data):
    """
    Conduct a Depth-First Search (DFS) on producers linked to a file.
    
    Given a file path, this function explores the associated producers using a DFS approach.
    It retrieves a list of producers connected to the file.

    Parameters:
    - file_path (str): The path to the file of interest.
    - memo (dict): A dictionary used for memoization to store visited file names.
    - memo_file_path (unused in this code): Presumably a dictionary to store file paths. Unused in current context.
    - memo_file_meta_data (dict): A dictionary containing meta-data associated with file names.

    Returns:
    - list: A list of cleaned producer names. Returns None if no producers are found.

    Note:
    The function seems to rely on certain structures in the meta-data dictionary and uses regex to clean up the producer names.
    """

    # Extract the base name of the file, then split it into the name and its postfix (extension)
    file_name = os.path.basename(file_path)
    file_name, postfix = os.path.splitext(file_name)
    
    # Check if the file name has already been visited (memoization)
    if file_name in memo:
        return
    
    # If the file name hasn't been visited, mark it as visited and initialize its associated list to empty
    memo[file_name] = []    
    note_meta_data = memo_file_meta_data[file_name]
    note_producer = note_meta_data[file_name]['producer']
    
    # Return if there are no producers associated with the file
    if note_producer == [] or note_producer == None:
        return

    # Create a collection of producers associated with the file
    producer_collection = []
    for producer in note_producer:
        producer = producer.strip()
        producer_collection.append(producer)

    # Split the first producer in the collection by comma and space (", ")
    producer_substrings = producer_collection[0].split(", ")
    
    # Clean and extract producer names from substrings
    clean_producer_collection = []
    for substring in producer_substrings:
        substring = substring.strip()
    
        # Extract producer names enclosed in double square brackets (e.g., [[Producer Name]])
        extracted_string = re.findall(r"\[\[([\w\s.]+)\]\]", substring)
        if extracted_string:
            clean_producer_collection.append(extracted_string[0])
        else:
            # If the name isn't enclosed in double square brackets, add the raw substring
            clean_producer_collection.append(substring)
    
    return clean_producer_collection
