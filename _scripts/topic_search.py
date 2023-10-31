import re
import os
import os.path
from read_files import read_file
from config import template_folder

def topic_search(file_path: str, memo_file_paths: dict, memo_file_meta_data: dict) -> list:
    """
    Search for and format the unique topics associated with a given file.
    
    Given a file path, this function identifies and formats the associated topics, ensuring 
    to retrieve the most relevant ones based on distance from the source file.

    Parameters
    ----------
    - file_path (str): The path to the file of interest.
    - memo_file_paths (dict): A dictionary containing file paths indexed by their associated names.
    - memo_file_meta_data (dict): A dictionary containing meta-data associated with file names.

    Returns
    -------
    - list: A list of unique topic names. Returns None if no topics are found.

    Notes
    -----
    The function expects certain folder names like 'template_folder' to be 
    globally defined. Similarly, functions like 'read_file' should be defined elsewhere 
    in the code for this function to work correctly.
    """

    # Skip processing if the file is in the template folder
    if template_folder in file_path:
        return

    memo = {}
    topics = _topic_search(file_path, 0, memo, memo_file_paths, memo_file_meta_data)

    # Return if no topics are found
    if topics == None:
        return 

    topics_and_distances = []
    for value in topics.values():
        if value != []:
            for element in value:
                topics_and_distances.append(element)

    topic_list = []
    for element in topics_and_distances:
        topic, distance = element
        if topic_list == []:
            topic_list.append((topic, distance))
        else:
            for item in topic_list:
                topic_2, distance_2 = item
                if topic_2 == topic:
                    if distance_2 < distance:
                        topic_list.remove((topic_2, distance_2))
                        topic_list.append((topic, distance))
                else:
                    topic_list.append((topic, distance))
    
    sorted_tuple_list = sorted(topic_list, key=lambda x: x[1], reverse=True)

    unique_topics = []
    for topic in sorted_tuple_list:
        ref, distance = topic
        if ref not in unique_topics:
            unique_topics.append(ref) 
            
    if unique_topics == []:
        return
    
    new_topics = [f'[[{topic}]]' for topic in unique_topics]
    new_topic_string = " " + ", ".join(new_topics)
        
    # Update the original file
    file_string = read_file(f"{file_path}")
    new_file_string = re.sub(r"(?<=Topics:).*", new_topic_string, file_string)

    # Write to the file
    with open(file_path, "w", encoding='utf-8') as f:
        f.write(new_file_string)
    
    return unique_topics

def _topic_search(file_path, distance, memo, memo_file_paths, memo_file_meta_data):
    """
    Conduct a Depth-First Search (DFS) on topics linked to a file.
    
    Given a file path, this function explores the associated topics using a DFS approach.
    It retrieves a dictionary of topics mapped to their distances from the source file.

    Parameters
    ----------
    - file_path (str): The path to the file of interest.
    - distance (int): Current distance from the source file.
    - memo (dict): A dictionary used for memoization to store processed file names.
    - memo_file_paths (dict): A dictionary containing file paths indexed by their associated names.
    - memo_file_meta_data (dict): A dictionary containing meta-data associated with file names.

    Returns
    -------
    - dict: A dictionary mapping topic names to their respective distances. Returns None in case of exceptions.

    Note
    ----
    The function utilizes regular expressions to extract topic names.
    """
    
    try:
        file_name = os.path.basename(file_path)
        file_name, postfix = os.path.splitext(file_name)

        # Base case 1
        if file_name in memo:
            return
        
        memo[file_name] = []

        topic_meta_data = memo_file_meta_data[file_name]
        topic_list = topic_meta_data[file_name]['topic']

        # Base case 2
        if topic_list == [] or topic_list == None:
            return
        
        for topic_text in topic_list:
            substring = topic_text.strip()
        
            if substring:
                extracted_string = re.findall(r"\[\[([\w\s.]+)\]\]", substring)
                if extracted_string:
                    memo[file_name].append((extracted_string, distance+1))
                if not extracted_string or extracted_string == []:
                    memo[file_name].append((substring, distance+1))

                file_path = memo_file_paths[topic_text]
                _topic_search(file_path, distance+1, memo, memo_file_paths, memo_file_meta_data)
    
    except:
        return

    return memo