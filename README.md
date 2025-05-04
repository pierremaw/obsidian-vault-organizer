# Obsidian Vault Organizer · Dynamic‑Programming‑Driven File Organization in Python

https://github.com/user-attachments/assets/840e9d63-2572-48f4-958c-0f43ffa524d6

**Obsidian Vault Organizer** is a Python automation script that transforms an Obsidian vault into a self‑maintaining knowledge graph.  It explores
recursion, file‑system manipulation, **and a memoised dynamic‑programming (DP) approach** to decide—once and only once—where every note *optimally* belongs.

Under the hood, each note becomes a *state* keyed by its metadata.  The script builds a DP table that maps that state to a folder path, caching the result so repeated look‑ups run in **O(1)** instead of repeatedly traversing the vault.  The payoff: a clean structure even for thousands of notes.

This project showcases my interest in algorithmic organisation—how DP, recursion, and metadata parsing can augment everyday tools like Obsidian.

---

## What the Script Does

When you run the script it:

* **Recursively traverses** your vault to discover every Markdown note.
* **Parses metadata**—tags such as `field`, `topic`, and `insight`—for each note.
* **Computes the optimal location** for every note via a DP lookup, then moves the file accordingly.
* **Eliminates clutter** by deleting empty folders and resolving circular topic references.
* **Refines relationships** with fuzzy‑string matching to keep topics semantically accurate.

The end result is a vault where *each note lives exactly where its metadata says it should*.

---

## Setup Instructions

1. **Install Obsidian** from [obsidian.md](https://obsidian.md/).

2. **Create or open a vault** (e.g. `~/ObsidianVault`).

3. **Clone this repository** *inside* that vault.

4. **Configure Obsidian**:

   * **Attachments** → `_attachments/`
   * **Templates** core plugin → enabled
   * **Template folder** → `_templates/`
   * (Optional) set a hotkey for “Insert template”.

5. **Open the vault** in VS Code (or your favourite IDE).

6. **Ensure** your terminal’s working directory is the vault root.

7. **Install Python 3** and the only dependency:

   ```bash
   pip install rapidfuzz
   # or, with the lockfile
   pip install -r requirements.txt
   ```

8. **Configure paths** in `config.py` (if you deviate from the defaults):

   ```python
   vault_path           = "./"             # root of your vault
   template_folder      = "_templates/"    # where templates live
   field_folder         = "1 Fields/"      # high‑level categories
   topic_folder         = "2 Topics/"      # topic subfolders
   key_insights_folder  = "3 Key Insights/"  # special insights
   ```

9. **Run the organiser** from the vault root:

   ```bash
   python _scripts/vault_organizer.py
   ```

---

## Architecture and Core Functions

### Core Folders (never deleted)

* `_templates/`
* `1 Fields/`
* `2 Topics/`
* `3 Key Insights/`

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

---

## Pro Tips

* **Back up** your vault before the first run, especially if you’re changing metadata conventions.
* For one‑command tidying, add an alias to `~/.zshrc` or `~/.bashrc`:

  ```bash
  alias obsidian-clean="cd $HOME/ObsidianVault && python _scripts/vault_organizer.py"
  ```

