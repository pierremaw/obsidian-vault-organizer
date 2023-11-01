# Vault Organizer

https://github.com/pierremaw/Obsidian-Vault-Organizer/assets/99075249/46bac793-d696-49f3-b0d8-d096e24f1238

## Introduction
Welcome to the Vault Organizer! I created this script as I was fascinated by recursion and dynamic programming, and I wanted to visualize them in action.

The Vault Organizer is a Python utility script that can organize, update, and maintain an Obsidian Vault. 

## What does the script do?
The script:
1. Traverses a configurable set of folders within an Obsidian Vault.
2. Scans the folders for notes that have the `.md` postfix.  
3. Categorizes notes based on tag metadata.
4. Then organizes notes in the file system hierarchy to ensure that they in the proper position based on their tag and their ancestor.

## Setup instructions
1. Ensure you have Obsidian installed. The latest version is available at https://obsidian.md/.
2. Create an Obsidian Vault (a folder to store all your Obsidian notes). I've named mine `ObsidianVault` and put it in my home folder.
3. Clone this GitHub repository into your Obsidian Vault.
4. In Obsidian, access `Settings`, click the `Files & Links` option, then change the default location for new attachments to `_attachments` (create this folder if it doesn't exist).
5. Set up templates:
   1. Within Obsidian, access `Settings`, click the `Core plugins` option, then within that section search for the `Templates` option and switch it on.
   2. Access `Settings`, click on `Templates`, then within that section update the `Template folder location` to `_templates`.
   3. Optional hotkey setup: Access `Settings`, click on the `Hotkeys` option, then update the hotkey for `Templates: Insert template` to `CTRL` + `ALT` + `T` (or any appropriate hotkey combination). 
6. Access Visual Studio Code (or any IDE).
7. Ensure you are in the root folder for your Obsidian Vault. Within Visual Studio Code, you can open your root folder by:
   1. Clicking `File`.
   2. Clicking the `Open Folder` option.
   3. Navigating to the appropriate folder.
   4. Then clicking the `Select Folder` option.
9. Ensure you have Python 3.x.
10. Install the Python library called `rapidfuzz`.
   ```bash
   pip install rapidfuzz

   or

   pip install -r requirements.txt
   ```
11. The helper script can then run from your Obsidian Vault:
   ```bash
   python _scripts/vault_organizer.py
   ``` 

## Configuration
Before running the script, ensure you've configured your vault settings in the `config.py` file:
- `vault_path`: The path to the root folder of your vault.
- `template_folder`: The name of the folder containing templates.
- `field_folder`: The name of the folder containing field notes.
- `topic_folder`: The name of the folder containing topic notes.
- `key_insights_folder`: The name of the folder container key insights.

## Key Component Functions

1. **CORE_FOLDERS**: A list containing folder paths that are protected from deletion.
2. **memo dictionaries**: These global dictionaries store memo file paths, metadata, types, and folder paths.

### Functions:

- **update_memo_variables(vault_path)**: Update global dictionaries with memo file paths, metadata, types, and folder paths.

- **vault_organizer(root_dir)**: Organize the vault structure by moving files to their respective folders based on their type and metadata.

- **update_topics(memo_file_paths, memo_file_meta_data)**: Traverses over memo files and updates their topics using the `topic_search` function.

- **delete_circular_topics_call(memo_file_paths, memo_file_meta_data)**: Traverses over memo files and deletes circular topics using the `delete_circular_topics` function.

- **delete_empty_folders(memo_folder_paths)**: Traverses the vault and deletes folders if they are empty, with the exception of paths provided in CORE_FOLDERS.

## Usage

Make sure you are in the root directory that contains the `_scripts` folder. Then, run the script using Python:

```bash
python _scripts/vault_organizer.py
```

## Tip

- Make sure to backup your vault before running the script.
