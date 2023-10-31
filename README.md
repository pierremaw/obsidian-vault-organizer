# Obsidian-Vault-Organizer

Organize Vault Structure Module

This Python module is designed to organize and manage the structure of a vault, which is a collection of memo files. The module provides several functions to manipulate and organize these files based on their metadata and types.
Functions
update_memo_variables(vault_path)

This function updates global dictionaries with memo file paths, metadata, types, and folder paths. It takes the path to the vault directory as an argument.
organize_vault_structure(root_dir)

This function organizes the vault structure by moving files to their respective folders based on their type and metadata. It takes the root directory of the vault as an argument.
update_topics(memo_file_paths, memo_file_meta_data)

This function updates topics for the provided memo files. It iterates over the provided memo files and updates their topics by calling the topic_search function. It takes a dictionary containing the paths of the memo files and a dictionary containing metadata for the memo files as arguments.
delete_circular_topics_call(memo_file_paths, memo_file_meta_data)

This function removes circular topics from the provided memo files. It iterates over the provided memo files and deletes circular topics by calling the delete_circular_topics function. It takes a dictionary containing the paths of the memo files and a dictionary containing metadata for the memo files as arguments.
delete_empty_folders(memo_folder_paths)

This function deletes empty folders from the vault, excluding specified protected folders. It traverses the vault and deletes folders if they are empty, with the exception of paths provided in CORE_FOLDERS. It takes a list containing the paths of the folders to check as an argument.
Usage

The main functions are called at the end of the module:

These functions are designed to be used together to manage and organize the vault structure. They should be called in the order shown above to ensure the vault is properly organized and updated.
