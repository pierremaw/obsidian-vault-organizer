# Obsidian Vault Organizer

https://github.com/user-attachments/assets/4b388696-c844-4a45-bf9f-7e5fc5025848

**Obsidian Vault Organizer** is a Python automation script that turns an Obsidian vault into a *self‑tidying* folder hierarchy.  It uses file‑system exploration, recursion, and dynamic programming to place notes in a file hierarchy based on their tagged *type* and *topic*.

Under the hood, each note’s metadata is cached in dictionaries on the first walk through the vault. Those caches let subsequent look‑ups run in **O(1)** during the *same* execution, instead of repeatedly traversing the tree. The payoff: a clean structure even when you have thousands of notes.

This project showcases my interest in algorithmic organisation—how caching, recursion, fuzzy matching and metadata parsing can partially automate everyday tools like Obsidian.

## What the Script Does

When you run the script it:

* **Recursively traverses** your vault once to index every Markdown note.
* **Caches metadata**—tags such as `topic`, and `type`—in in‑memory lookup tables.
* **Computes a destination folder** for every note:  
  * `field` notes become top‑level folders.  
  * `topic` notes are filed under the closest‑matching field using **fuzzy‑string heuristics**.
* **Propagates relationships** with a depth‑first search that rewrites `Topics:` links so each note inherits the right upstream topics.
* **Eliminates clutter** by deleting empty folders and removing *circular* topic references (notes that list themselves as a topic).

The result is a vault where *each note lives exactly where its metadata says it should*—and the links inside the notes stay in sync with the folder layout.

## Setup Instructions

1. **Install Obsidian** from [obsidian.md](https://obsidian.md/).

2. **Create or open a vault** (e.g. `~/ObsidianVault`).

3. **Clone this repository** *inside* that vault.

4. **Configure Obsidian**:

   * **Attachments** → `_attachments/`
   * **Templates** core plugin → enabled
   * **Template folder** → `_templates/`
   * (Optional) set a hotkey for “Insert template”.

5. **Open the vault** in VS Code (or your favourite IDE).

6. **Ensure** your terminal’s working directory is the vault root.

7. **Install Python 3** and the only dependency:

   ```bash
   pip install rapidfuzz
   # or, with the lockfile
   pip install -r requirements.txt
   ```

8. **Configure paths** in `config.py` (if you deviate from the defaults):

   ```python
   vault_path      = "./"          # root of your vault
   template_folder = "_templates/" # where templates live
   field_folder    = "1 Fields/"   # high‑level categories
   ```

9. **Run the organiser** from the vault root:

   ```bash
   python _scripts/vault_organizer.py
   ```

## Architecture and Core Functions

### Core Folders (never deleted)

* `_templates/`
* `1 Fields/`

### Key Data Structures

| Name                  | Role                                |
| --------------------- | ----------------------------------- |
| `memo_file_paths`     | Maps note → current path (DP cache) |
| `memo_file_meta_data` | Maps note → metadata                |
| `memo_file_types`     | Groups notes by semantic type       |
| `memo_folder_paths`   | Indexes all folders in the vault    |

### Major Functions

| Function                        | Purpose                                                                  |
| ------------------------------- | ------------------------------------------------------------------------ |
| `update_memo_variables()`       | Refreshes all global memo dictionaries.                                  |
| `vault_organizer()`             | Computes each note’s destination via DP + fuzzy matching, then moves it. |
| `update_topics()`               | Rewrites topic links using depth‑first search.                           |
| `delete_circular_topics_call()` | Removes self‑referential tags.                                           |
| `delete_empty_folders()`        | Deletes any folder not in the core set *and* left empty.                 |

## Pro Tips

* For one‑command tidying, add an alias to `~/.zshrc` or `~/.bashrc`:

  ```bash
  alias obsidian-clean="cd $HOME/ObsidianVault && python _scripts/vault_organizer.py"
  ```
