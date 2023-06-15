
import re
import os
import os.path
from collections import deque

from read_files import read_file

'''
DELETE CIRCULAR TOPICS FUNCTION
'''
def delete_circular_topics(file_path: str, memo_file_meta_data: dict) -> None:
    '''
    Searches for circular topics in a file and deletes them
    '''
    
    # get the note name
    note_name = os.path.basename(file_path)
    note_name = os.path.splitext(note_name)
    note_name = note_name[0]
    
    note_meta_data = memo_file_meta_data[note_name]
    
    # get the topics from the note_meta_data
    note_topics = note_meta_data[note_name]['topic']

    queue = deque(note_topics)
    unique_topics = []
    
    while queue:
        topic = queue.popleft()
        if topic != note_name:
            unique_topics.append(topic)

    if len(unique_topics) == len(note_topics):
        return

    new_topics = [f'[[{topic}]]' for topic in unique_topics]
    new_topic_string = " " + ", ".join(new_topics)

    file_string = read_file(f"{file_path}")
    new_file_string = re.sub(r"(?<=Topics:).*", new_topic_string, file_string)
        # write to the file
    with open(file_path, "w") as f:
        f.write(new_file_string)

    return