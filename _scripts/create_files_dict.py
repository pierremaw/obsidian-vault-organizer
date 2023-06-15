import os
import os.path
from meta_data_search import _meta_data_search
from config import vault_path, template_folder_name

'''
ADD NOTE TO QUEUE
'''
def add_note(queue, note, type_):
    if type_ not in queue:
        queue[type_] = []
    queue[type_].append(note)

'''
CREATE FILES DICT
'''
def create_files_dict(directory: str) -> dict:
    '''
    Traverse the directory and create a dictionary. 
    The key for the dictionary is the file name and the value is the file path
    '''
    # create a dictionary
    memo_file_paths, memo_file_meta_data, memo_file_types, memo_folder_paths = {}, {}, {}, {}

    # traverse the directory
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if file_path.endswith(".md"):
                if template_folder_name in file_path:
                    continue
                
                # file_name_clean
                file_name_clean, postfix = os.path.splitext(filename)
            
                # memo_file_paths
                memo_file_paths[file_name_clean] = file_path

                # memo_file_meta_data
                note_meta_data = _meta_data_search(file_path, {})
                memo_file_meta_data[file_name_clean] = note_meta_data

                # memo_file_types
                note_type = note_meta_data[file_name_clean]['type']

                if note_type:
                    try:
                        note_type = note_type[0].strip()
                        if 'source' in note_type:
                            note_type = 'source'
                        add_note(memo_file_types, file_name_clean, note_type)

                    except:
                        pass
                    
    return memo_file_paths, memo_file_meta_data, memo_file_types, memo_folder_paths


