# Obsidian Vault Organizer: Dynamic Programming File Structuring with Python Automation

[Watch a demo of the automation in action.](https://github.com/pierremaw/Obsidian-Vault-Organizer/assets/99075249/46bac793-d696-49f3-b0d8-d096e24f1238)

Obsidian Vault Organizer is a Python automation script I created to explore recursion, file system manipulation, and dynamic programming concepts within a real-world note-taking workflow. It parses, categorizes, and restructures a personal Obsidian Vault by analyzing metadata tags in `.md` files. The automation dynamically organizes notes into structured folders based on their semantic relationships and tag hierarchy—turning a flat note space into a clean, maintainable knowledge graph.

This project reflects my interest in recursive systems, metadata processing, and how file automation can augment tools like Obsidian to support more meaningful long-term organization.

## What the Script Does

Once executed, the script:

- Recursively traverses your configured vault folder to find Markdown notes.
- Extracts metadata from each note, including tags such as `field`, `topic`, and `insight`.
- Uses that metadata to move and restructure files into folders based on their type and relational context.
- Cleans up the workspace by removing empty folders and eliminating circular topic references.
- Updates memo-topic relationships using a fuzzy string matching algorithm for semantic accuracy.

The result is a neatly organized vault, where each note exists exactly where it should, guided by its metadata and relational structure.

## Setup Instructions

1. Install Obsidian from [obsidian.md](https://obsidian.md/).
2. Create or open your vault (e.g., `~/ObsidianVault`).
3. Clone this repository into the vault directory.
4. Configure Obsidian settings:
   - Set the default location for attachments to `_attachments/`.
   - Enable the `Templates` core plugin.
   - Set your template folder location to `_templates/`.
   - Optionally configure a hotkey for inserting templates.
5. Open the vault in VS Code or your IDE of choice.
6. Ensure you're in the root directory of your Obsidian Vault.
7. Install Python 3.x and the `rapidfuzz` dependency:
   ```bash
   pip install rapidfuzz
   # or
   pip install -r requirements.txt
````

8. Configure folder paths in `config.py`:

   * `vault_path`: The root path to your vault (`./` by default).
   * `template_folder`: Where templates are stored (e.g., `_templates/`).
   * `field_folder`: High-level category folders (e.g., `1 Fields/`).
   * `topic_folder`: Topical subfolders (e.g., `2 Topics/`).
   * `key_insights_folder`: Special insights (e.g., `3 Key Insights/`).

9. Run the organizer script from the vault root:

   ```bash
   python _scripts/vault_organizer.py
   ```

## Architecture and Core Functions

### Core Folders

The following folders are protected from cleanup and are central to the file system structure:

* `_templates/`
* `1 Fields/`
* `2 Topics/`
* `3 Key Insights/`

### Key Data Structures

Global dictionaries store state during execution:

* `memo_file_paths`: Tracks file locations.
* `memo_file_meta_data`: Stores tag and type metadata.
* `memo_file_types`: Organizes files by their semantic category.
* `memo_folder_paths`: Indexes folders across the vault.

### Major Functions

#### `update_memo_variables(vault_path)`

Scans the vault to refresh global dictionaries based on the current file and folder structure.

#### `vault_organizer(root_dir)`

Moves notes into new folders according to their `field` or `topic` metadata. Uses fuzzy string matching to map topics to fields with contextual accuracy.

#### `update_topics(memo_file_paths, memo_file_meta_data)`

Traverses each memo and updates its topics using logic defined in the external `topic_search` module.

#### `delete_circular_topics_call(memo_file_paths, memo_file_meta_data)`

Removes redundant or self-referencing tags to maintain clean semantic hierarchy.

#### `delete_empty_folders(memo_folder_paths)`

Removes unused folders unless they are part of the protected core folder set.

## Pro Tips

* Always backup your vault before running the script, especially if you’re testing changes to metadata conventions.
* For faster CLI access, you can alias the script in your `.zshrc` or `.bashrc`:

  ```bash
  alias obsidian="cd $HOME/ObsidianVault && python _scripts/vault_organizer.py"
  ```

## Why I Built This

I’ve always been intrigued by how recursive logic and metadata parsing can create intelligent systems from unstructured content. Obsidian Vault Organizer is an experiment in building such a system—one that adapts and restructures a living knowledge base through automation. It’s also a practical way to keep a growing collection of notes navigable and meaningful over time.

The vault organizer isn't in active use but it was a fun experiment to explore recursion and dynamic programming. 
