import os
import os.path
from meta_data_search import _meta_data_search
from config import vault_path, template_folder_name
template_dir = template_folder_name.rstrip('/')

def add_note(queue, note, type_):
    """
    Add a note to a queue.

    Parameters
    ----------
    - queue (dict): The queue to which the note should be added.
    - note (str): The note to be added.
    - type_ (str): The type of the note.
    """
    if type_ not in queue:
        queue[type_] = []
    queue[type_].append(note)

def create_files_dict(directory: str) -> dict:
    """
    Traverse a directory and create a dictionary mapping file names to file paths.

    The function ignores files in the '_templates' folder and files that do not have the '.md' extension.

    Parameters
    ----------
    - directory (str): The directory to traverse.

    Returns:
    - dict: A dictionary where the keys are file names and the values are file paths.
    """
    memo_file_paths, memo_file_meta_data, memo_file_types, memo_folder_paths = {}, {}, {}, {}
    print(f"Template folder name from config: {template_dir}")

    for dirpath, dirnames, filenames in os.walk(directory):
        # Check if the current directory is the template directory
        if template_dir in os.path.relpath(dirpath, directory).split(os.path.sep):
            print(f"Skipping directory: {dirpath}")
            continue

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if file_path.endswith(".md") and not os.path.join(directory, template_dir) in file_path:
                file_name_clean, postfix = os.path.splitext(filename)
                memo_file_paths[file_name_clean] = file_path
                note_meta_data = _meta_data_search(file_path, {})
                memo_file_meta_data[file_name_clean] = note_meta_data
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