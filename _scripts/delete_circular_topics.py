import re
import os
import os.path
from collections import deque

from read_files import read_file

def delete_circular_topics(file_path: str, memo_file_meta_data: dict) -> None:
    """
    Searches for and deletes circular topics within a given file.
    
    This function checks the topics of a note and ensures that the note's own name is not listed 
    as one of its topics. If it finds such a "circular topic", it removes it.

    Parameters
    ----------
    - file_path (str): The path to the file in which circular topics should be deleted.
    - memo_file_meta_data (dict): Dictionary containing metadata for the memo files.

    Returns
    -------
    - None: The function modifies the content of the file in-place and does not return any value.
    """
    
    # Get the note name
    note_name = os.path.basename(file_path)
    note_name = os.path.splitext(note_name)
    note_name = note_name[0]
    
    note_meta_data = memo_file_meta_data[note_name]
    
    # Get the topics from the note_meta_data
    note_topics = note_meta_data[note_name]['topic']

    queue = deque(note_topics)
    unique_topics = []
    
    while queue:
        topic = queue.popleft()
        if topic != note_name:
            unique_topics.append(topic)

    # If no circular topics were found, return early
    if len(unique_topics) == len(note_topics):
        return

    # Create a new topic string to replace the old one
    new_topics = [f'[[{topic}]]' for topic in unique_topics]
    new_topic_string = " " + ", ".join(new_topics)

    # Read the file content and replace the old topic string with the new one
    file_string = read_file(f"{file_path}")
    new_file_string = re.sub(r"(?<=Topics:).*", new_topic_string, file_string)
    
    # Write the modified content back to the file
    with open(file_path, "w") as f:
        f.write(new_file_string)

    return
