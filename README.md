# Obsidian Vault Organizer

[https://github.com/user-attachments/assets/b8f4986e-61c3-4c1a-81df-f2e13223f948](https://github.com/user-attachments/assets/b8f4986e-61c3-4c1a-81df-f2e13223f948)

**Obsidian Vault Organizer** is a Python-powered automation tool that transforms an Obsidian vault into a self-organizing folder system. By analyzing metadata tags such as `type` and `topic`, it uses recursion, dynamic programming, and file system traversal to intelligently reposition notes. The result is a vault where every note is filed in the folder that best reflects its semantic purpose.

To improve performance, the script builds metadata caches on the first traversal, allowing all subsequent lookups to run in constant time. This means even large vaults with thousands of notes can be neatly organized without performance bottlenecks. This project also serves as a practical case study in recursion, fuzzy string matching, and structured metadata parsing.

## Features

Running the script performs the following operations:

* Traverses the entire vault recursively to index Markdown notes.
* Caches all relevant metadata, including tags like `topic` and `type`, in memory.
* Assigns destination folders:

  * Notes tagged as `field` become top-level folders.
  * `topic` notes are placed within the closest-matching field using fuzzy string heuristics.
* Updates topic references using depth-first search, ensuring hierarchical consistency.
* Removes empty folders and eliminates circular topic references, such as notes that cite themselves.

The script ensures that each note lives precisely where its metadata dictates—and updates internal links to match the new structure.

## Getting Started

### Prerequisites

* Install [Obsidian](https://obsidian.md/).
* Create or open a vault (e.g., `~/ObsidianVault`).
* Ensure Python 3 is installed on your system.

### Installation

1. Clone this repository into your Obsidian vault:

   ```bash
   git clone https://github.com/your-repo/obsidian-vault-organizer.git
   ```

2. Open the vault in your preferred IDE (e.g., VS Code) and set the terminal’s working directory to the vault root.

3. Install the required Python dependency:

   ```bash
   pip install rapidfuzz
   ```

   Or, to use the provided lockfile:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure paths in `config.py` if needed:

   ```python
   vault_path      = "./"          # Root of your vault
   template_folder = "_templates/" # Template directory
   field_folder    = "1 Fields/"   # Folder for high-level categories
   ```

5. Run the organizer script:

   ```bash
   python _scripts/vault_organizer.py
   ```

### Recommended Obsidian Settings

* Set attachment folder to `_attachments/`.
* Enable the core Templates plugin.
* Set template folder path to `_templates/`.
* Optionally, assign a hotkey for "Insert template".

## Architecture

### Directory Structure

* `_templates/`: Stores reusable content templates.
* `1 Fields/`: High-level folder hierarchy based on note metadata.

### Core Data Structures

| Variable              | Description                          |
| --------------------- | ------------------------------------ |
| `memo_file_paths`     | Maps notes to their current paths    |
| `memo_file_meta_data` | Stores parsed metadata for each note |
| `memo_file_types`     | Categorizes notes by semantic type   |
| `memo_folder_paths`   | Indexes all folders across the vault |

### Key Functions

| Function Name                   | Description                                                           |
| ------------------------------- | --------------------------------------------------------------------- |
| `update_memo_variables()`       | Refreshes all global caches                                           |
| `vault_organizer()`             | Calculates new locations using DP and fuzzy matching, and moves notes |
| `update_topics()`               | Rewrites topic links via depth-first search                           |
| `delete_circular_topics_call()` | Removes notes that list themselves as topics                          |
| `delete_empty_folders()`        | Deletes non-core folders that are empty                               |

## Tips and Tricks

Certainly. Here's the clarified version of that section with an added explanatory sentence to improve usability:

---

## Tips and Tricks

To simplify future usage, you can create a shell alias that lets you run the organizer with a single command from any terminal session. Add the following line to your `~/.bashrc`, `~/.zshrc`, or equivalent shell configuration file:

```bash
alias obsidian-clean="cd $HOME/ObsidianVault && python _scripts/vault_organizer.py"
```

After saving the file, reload your shell or run `source ~/.bashrc` (or `source ~/.zshrc`) to apply the change. Now, typing `obsidian-clean` will automatically navigate to your vault and run the organizer script.
