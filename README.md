# Vault Organizer README

https://github.com/pierremaw/Obsidian-Vault-Organizer/assets/99075249/35a4d679-f439-44d7-91f3-65764d81896d

## Introduction
The Vault Organizer is a Python utility script aimed at organizing, updating, and maintaining a structured file vault. This vault is composed of markdown memo files with distinct types and metadata. The script provides functionalities such as:
- Moving files based on their types and metadata to respective folders.
- Updating topics within the memo files.
- Removing circular topics from the memo files.
- Deleting empty folders while ensuring core folders remain protected.

## Prerequisites
- Python 3.x
- Libraries: `os`, `shutil`, `rapidfuzz`, `collections`

## Installation
1. Clone this repository.
2. Navigate to the root directory.
3. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
Before running the script, ensure you've configured your vault settings in the `config.py` file:
- `vault_path`: The path to the root directory of your vault.
- `field_folder`: The name of the folder containing field notes.
- `topic_folder`: The name of the folder containing topic notes.
- `template_folder`: The name of the folder containing templates.
- `key_insights_folder`: The name of the folder container key insights.

## Key Components & Their Functions

1. **CORE_FOLDERS**: A list containing folder paths that are protected from deletion.
2. **memo dictionaries**: These global dictionaries store memo file paths, metadata, types, and folder paths.

### Functions:

- **update_memo_variables(vault_path)**: Update global dictionaries with memo file paths, metadata, types, and folder paths.

- **vault_organizer(root_dir)**: Organize the vault structure by moving files to their respective folders based on their type and metadata.

- **update_topics(memo_file_paths, memo_file_meta_data)**: Iterates over memo files and updates their topics using the `topic_search` function.

- **delete_circular_topics_call(memo_file_paths, memo_file_meta_data)**: Iterates over memo files and deletes circular topics using the `delete_circular_topics` function.

- **delete_empty_folders(memo_folder_paths)**: Traverses the vault and deletes folders if they are empty, with the exception of paths provided in CORE_FOLDERS.

## Usage

Make sure you are in the root directory that contains the `_scripts` folder. Then, run the script using Python:

```bash
python _scripts/vault_organizer.py
```

## Notes

- Make sure to backup your vault before running the script to avoid any unintentional data loss.
- If any error occurs during the file movement process within the `vault_organizer` function, the script continues to process the next file.
- Some important functionalities like `create_files_dict`, `topic_search`, and `delete_circular_topics` are imported from other modules, ensure they're present in the same directory.

## License
[MIT](https://choosealicense.com/licenses/mit/)
