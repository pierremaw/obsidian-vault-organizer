# Vault Organizer

https://github.com/pierremaw/Obsidian-Vault-Organizer/assets/99075249/46bac793-d696-49f3-b0d8-d096e24f1238

## Introduction
Welcome to the Vault Organizer! I created this script because I was fascinated by recursion and dynamic programming, and I wanted to visualize them in action.

The Vault Organizer is a Python utility script aimed at organizing, updating, and maintaining an obsidian file vault. This vault is composed of markdown notes with distinct types and metadata. The script provides functionalities such as:
- Moving files based on their types to respective folders.
- Updating topics within the note files.
- Removing circular topics from the note files.
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

## Tip

- Make sure to backup your vault before running the script.
