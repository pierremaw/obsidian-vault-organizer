import os
from collections import defaultdict
from meta_data_search import _meta_data_search
from config import vault_path, template_folder

template_dir = template_folder.rstrip('/')

def add_note(queue: defaultdict, note: str, type_: str) -> None:
    """
    Add a note to a queue.

    Parameters
    ----------
    queue : defaultdict
        The queue to which the note should be added.
    note : str
        The note to be added.
    type_ : str
        The type of the note.
    """
    if type_ not in queue:
        queue[type_] = []
    queue[type_].append(note)

def create_files_dict(directory: str) -> dict:
    """
    Traverse a directory and create a dictionary mapping file names to file paths, ignoring certain templates.

    Parameters
    ----------
    directory : str
        The directory to traverse.

    Returns
    -------
    tuple
        A tuple containing dictionaries of file paths, meta-data, types, and folder paths.
    """
    memo_file_paths, memo_file_meta_data, memo_file_types, memo_folder_paths = {}, {}, {}, {}


    for dirpath, dirnames, filenames in os.walk(directory):
        if template_dir in os.path.split(dirpath):
            continue
        for filename in filenames:
            if filename.endswith(".md"):
                file_path = os.path.join(dirpath, filename)
                file_name_clean = os.path.splitext(filename)[0]
                
                memo_file_paths[file_name_clean] = file_path
                note_meta_data = _meta_data_search(file_path, {})
                memo_file_meta_data[file_name_clean] = note_meta_data

                note_type = note_meta_data.get(file_name_clean, {}).get('type')
                if note_type:
                    note_type = note_type[0].strip()
                    if 'source' in note_type:
                        note_type = 'source'
                    add_note(memo_file_types, file_name_clean, note_type)

    return memo_file_paths, memo_file_meta_data, memo_file_types, memo_folder_paths
