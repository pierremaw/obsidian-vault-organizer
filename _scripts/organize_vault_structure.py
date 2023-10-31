import os
import os.path
import shutil
from rapidfuzz import fuzz
from collections import deque

from create_files_dict import create_files_dict

from topic_search import topic_search
from delete_circular_topics import delete_circular_topics
from config import vault_path, field_folder_name, topic_folder, template_folder_name

# Define the core folders that are protected from deletion
CORE_FOLDERS = [
    "_templates/",
    "1 Fields/",
    "2 Topics/",
    "3 Key Insights/"
]

# Global dictionaries to store memo file paths, metadata, types, and folder paths
memo_file_paths = {}
memo_file_meta_data = {}
memo_file_types = {}
memo_folder_paths = {}

def update_memo_variables(vault_path):
    """
    Update global dictionaries with memo file paths, metadata, types, and folder paths.

    Parameters
    ----------
    - vault_path (str): The path to the vault directory.
    """

    global memo_file_paths, memo_file_meta_data, memo_file_types, memo_folder_paths
    memo_file_paths, memo_file_meta_data, memo_file_types, memo_folder_paths = create_files_dict(vault_path)

def organize_vault_structure(root_dir):
    """
    Organize the vault structure by moving files to their respective folders based on their type and metadata.

    Parameters
    ----------
    - root_dir (str): The root directory of the vault.
    """
    if 'field' in memo_file_types:
        for note_name in memo_file_types['field']:
            try:
                field_instance_folder = f"{vault_path}{field_folder_name}{note_name}/"
                check_folder_path = os.path.isdir(field_instance_folder)
                if not check_folder_path:
                    os.mkdir(field_instance_folder)
                file_path = memo_file_paths[note_name]
                destination_path = field_instance_folder+f"{note_name}.md"
            
                if file_path != destination_path:
                    shutil.move(file_path, destination_path)
                    memo_file_paths[note_name] = destination_path    
            except:
                continue

    if 'topic' in memo_file_types:
        for note_name in memo_file_types['topic']:
            try:
                note_parent_type = 'field'
                note_type = 'topic'
                file_path = memo_file_paths[note_name]
                note_meta_data = memo_file_meta_data[note_name]
                note_topics = note_meta_data[note_name]['topic']
                field_collection = [note_topics[0]]
                field_collection_queue = deque(field_collection)
                selected_field = None
                best_fuzzy_match = float('-inf')
                
                while field_collection_queue:
                    current_field = field_collection_queue.pop()
                    current_ratio = fuzz.ratio(current_field, note_name)
                    if current_ratio > best_fuzzy_match:
                        best_fuzzy_match = current_ratio
                        selected_field = current_field

                target_folder_path = os.path.join(vault_path, field_folder_name, selected_field, note_name)
                if not os.path.exists(target_folder_path):
                    os.makedirs(target_folder_path, exist_ok=True)      

                current_file_path = memo_file_paths[note_name]
                destination_path = f'{target_folder_path}/'+f"{note_name}.md"
                
                if current_file_path != destination_path:
                    shutil.move(current_file_path, destination_path)
                    memo_file_paths[note_name] = destination_path

                target_folder_path = os.path.join(vault_path, topic_folder, note_name)
                if not os.path.exists(target_folder_path):
                    os.makedirs(target_folder_path, exist_ok=True)    
        
            except:
                # print(f'Fix topic section, {note_name}')
                continue
        
    if 'subtopic' in memo_file_types:
        for note_name in memo_file_types['subtopic']:
            try:
                note_parent_type = 'topic'
                note_type = 'subtopic'  
                file_path = memo_file_paths[note_name]         
                note_meta_data = memo_file_meta_data[note_name]
                note_topics = note_meta_data[note_name]['topic']
                
                topic_collection = []
                for topic_note in note_topics:
                    try:
                        topic_note = topic_note.strip()        
                        topic_file_path = memo_file_paths[topic_note]
                        topic_meta_data = memo_file_meta_data[topic_note]
                        topic_meta_data_type = topic_meta_data[topic_note]['type']
                        if topic_meta_data_type:
                            if topic_meta_data_type[0] == note_parent_type:
                                topic_collection.append(topic_note)
                    except:
                        # print(f'Fix topic meta data')
                        continue

                topic_collection_queue = deque(topic_collection)
                selected_topic = None
                best_fuzzy_match = float('-inf')
                while topic_collection_queue:
                    current_topic = topic_collection_queue.pop()
                    current_ratio = fuzz.ratio(current_topic, note_name)
                    if current_ratio > best_fuzzy_match:
                        best_fuzzy_match = current_ratio
                        selected_topic = current_topic
                selected_topic_meta_data = memo_file_meta_data[selected_topic]
                selected_topic_topics = selected_topic_meta_data[selected_topic]['topic']
                
                field_collection = []
                for topic_note in selected_topic_topics:
                    try:
                        topic_note = topic_note.strip()    
                        topic_meta_data = memo_file_meta_data[topic_note]
                        topic_meta_data_type = topic_meta_data[topic_note]['type']
                    
                        if topic_meta_data_type:
                            if topic_meta_data_type[0] == 'field':
                                field_collection.append(topic_note)
                    except:
                        # print(f'Fix topic meta data')
                        continue

                field_collection_queue = deque(field_collection)
                selected_field = None
                best_fuzzy_match = float('-inf')

                while field_collection_queue:
                    current_field = field_collection_queue.pop()
                    current_ratio = fuzz.ratio(current_field, note_name)
        
                    if current_ratio > best_fuzzy_match:
                        best_fuzzy_match = current_ratio
                        selected_field = current_field

                target_folder_path = os.path.join(vault_path, field_folder_name, selected_field, selected_topic, note_name)
                if not os.path.exists(target_folder_path):
                    os.makedirs(target_folder_path, exist_ok=True)      
        
                current_file_path = memo_file_paths[note_name]
                destination_path = f'{target_folder_path}/'+f"{note_name}.md"
                if current_file_path != destination_path:
                    shutil.move(current_file_path, destination_path)
                    memo_file_paths[note_name] = destination_path
            
                target_folder_path = os.path.join(vault_path, topic_folder, selected_topic, note_name)
                if not os.path.exists(target_folder_path):
                    os.makedirs(target_folder_path, exist_ok=True)      
        
            except:
                # print(f'Fix topic section, {note_name}')
                continue
    
    if 'microtopic' in memo_file_types:
        for note_name in memo_file_types['microtopic']:
            try:
                note_great_grandparent_type = 'field'
                note_grandparent_type = 'topic'
                note_parent_type = 'subtopic'
                note_type = 'microtopic'
            
                current_note_file_path = memo_file_paths[note_name]
                note_meta_data = memo_file_meta_data[note_name]
                note_topics = note_meta_data[note_name]['topic']
                note_type = note_meta_data[note_name]['type']

                if note_type:
                    note_type = note_type[0]

                subtopic_collection = []
                for topic_note in note_topics:
                    try:
                        topic_note = topic_note.strip()
                        topic_file_path = memo_file_paths[topic_note]
                        topic_meta_data = memo_file_meta_data[topic_note]
                        topic_meta_data_type = topic_meta_data[topic_note]['type']
                        if topic_meta_data_type:
                            if topic_meta_data_type[0] == note_parent_type:
                                subtopic_collection.append(topic_note)

                    except:
                        # print(f'Fix topic meta data')
                        continue

                subtopic_collection_queue = deque(subtopic_collection)
                selected_subtopic = None
                best_fuzzy_match = float('-inf')
                
                while subtopic_collection_queue:
                    current = subtopic_collection_queue.pop()
                    current_fuzzy_match = fuzz.ratio(current, note_name)
                    if current_fuzzy_match > best_fuzzy_match:
                        best_fuzzy_match = current_fuzzy_match
                        selected_subtopic = current

                selected_meta_data = memo_file_meta_data[selected_subtopic]
                selected_topics = selected_meta_data[selected_subtopic]['topic']
                
                collection = []

                if selected_topics:
                    for topic_note in selected_topics:
                        try:
                            topic_meta_data = memo_file_meta_data[topic_note]
                            topic_meta_data_type = topic_meta_data[topic_note]['type']
                            if topic_meta_data_type:
                                if topic_meta_data_type[0] == note_grandparent_type:
                                    collection.append(topic_note)
                        except:
                            # print(f'Fix topic meta data')
                            continue

                collection_queue = deque(collection)
                selected_topic = None
                best_fuzzy_match = float('-inf')
                while collection_queue:
                    current = collection_queue.pop()
                    current_fuzzy_match = fuzz.ratio(current, note_name)
                    if current_fuzzy_match > best_fuzzy_match:
                        best_fuzzy_match = current_fuzzy_match
                        selected_topic = current

                selected_meta_data = memo_file_meta_data[selected_topic]
                selected_topics = selected_meta_data[selected_topic]['topic']

                collection = []

                if selected_topics:
                    for topic_note in selected_topics:
                        try:
                            topic_meta_data = memo_file_meta_data[topic_note]
                            topic_meta_data_type = topic_meta_data[topic_note]['type']
                            if topic_meta_data_type:
                                if topic_meta_data_type[0] == note_great_grandparent_type: 
                                    collection.append(topic_note)
                        except:
                            # print(f'Fix topic meta data')
                            continue

                if len(collection) > 1:
                    collection_queue = deque(collection)
                    selected_field = None
                    best_fuzzy_match = float('-inf')
                    while collection_queue:
                        current = collection_queue.pop()
                        current_fuzzy_match = fuzz.ratio(current, note_name)
                        if current_fuzzy_match > best_fuzzy_match:
                            best_fuzzy_match = current_fuzzy_match
                            selected_field = current
                elif len(collection) == 1:
                    selected_field = collection[0]
        
                target_folder_path = os.path.join(vault_path, field_folder_name, selected_field, selected_topic, selected_subtopic)
                if not os.path.exists(target_folder_path):
                    os.makedirs(target_folder_path, exist_ok=True)              
            
                destination_path = f'{target_folder_path}/'+f"{note_name}.md"
                
                if current_note_file_path != destination_path:
                    shutil.move(current_note_file_path, destination_path)
                    memo_file_paths[note_name] = destination_path
        
            except:
                # print(f'Fix microtopic section, {note_name}')
                continue
                
    return True

def update_topics(memo_file_paths, memo_file_meta_data):
    """
    Updates topics for the provided memo files.

    Iterates over the provided memo files and updates their topics by calling the `topic_search` function.

    Parameters
    ----------
    - memo_file_paths (dict): A dictionary containing the paths of the memo files.
    - memo_file_meta_data (dict): A dictionary containing metadata for the memo files.
    """
    for k, v in memo_file_paths.items():
        topic_search(v, memo_file_paths, memo_file_meta_data)

def delete_circular_topics_call(memo_file_paths, memo_file_meta_data):
    """
    Removes circular topics from the provided memo files.

    Iterates over the provided memo files and deletes circular topics by calling the `delete_circular_topics` function.

    Parameters
    ----------
    - memo_file_paths (dict): A dictionary containing the paths of the memo files.
    - memo_file_meta_data (dict): A dictionary containing metadata for the memo files.
    """
    for v in memo_file_paths.values():
        delete_circular_topics(v, memo_file_meta_data)

def delete_empty_folders(memo_folder_paths):
    """
    Deletes empty folders from the vault, excluding specified protected folders.

    Helper function that traverses the vault and deletes folders if they are empty,
    with the exception of paths provided in CORE_FOLDERS.

    Parameters
    ----------
    - memo_folder_paths (list): A list containing the paths of the folders to check.
    """
    for root, dirs, files in os.walk(vault_path, topdown=False):
        for name in dirs:
            dir_path = os.path.join(root, name)
            # If the directory path matches one of the protected paths, skip it
            if dir_path in CORE_FOLDERS:
                continue
            # If the directory is empty, delete it
            elif not os.listdir(dir_path):
                os.rmdir(dir_path)

# Call main functions
update_memo_variables(vault_path)
delete_empty_folders(memo_folder_paths)
update_topics(memo_file_paths, memo_file_meta_data)
delete_circular_topics_call(memo_file_paths, memo_file_meta_data)
update_memo_variables(vault_path)
organize_vault_structure(vault_path)