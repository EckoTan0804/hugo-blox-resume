from datetime import datetime
from pathlib import Path
import argparse
import re


def to_title_case(s):
    minor_words = {
        "a",
        "an",
        "the",
        "and",
        "but",
        "or",
        "nor",
        "for",
        "so",
        "yet",
        "at",
        "by",
        "in",
        "on",
        "to",
        "up",
        "with",
        "as",
    }
    words = s.split("_")
    title_cased = [words[0].capitalize()] + [
        word if word.lower() in minor_words else word.capitalize() for word in words[1:]
    ]
    return " ".join(title_cased)


def to_kebab_case(s):
    return s.replace("_", "-")


def compute_dir_weight(prefix):
    if not isinstance(prefix, int):
        try:
            prefix = int(prefix)
        except ValueError:
            print("Error: Invalid prefix for directory weight computation")
            return None
    return prefix * 100


def compute_weight(prefix, count):
    if not isinstance(prefix, int):
        try:
            prefix = int(prefix)
        except ValueError:
            print("Error: Invalid prefix for file weight computation")
            return None
    return prefix * 100 + count


def main(target_dir, filenames):
    target_dir = Path(target_dir)

    # Extract prefix and name from target directory
    dir_match = re.match(r"^([0-9]+)_(.*)", target_dir.name)
    if not dir_match:
        print("Error: Invalid target directory format")
        return

    dir_prefix = int(dir_match.group(1))
    dir_name = dir_match.group(2)
    print(dir_name)

    # Convert directory name to title case and kebab case
    dir_title = to_title_case(dir_name)
    dir_tag = to_kebab_case(dir_name)

    # Extract parent directory name
    parent_dir = target_dir.parent
    parent_name = parent_dir.name
    parent_tag = to_kebab_case(parent_name)

    # Check if target directory exists, if not create it
    if not target_dir.exists():
        target_dir.mkdir(parents=True)
        # Create _index.md file with frontmatter
        with open(target_dir / "_index.md", "w") as f:
            f.write(
                f"""---
# ===== Title, summary, and position in the left sidebar =====
linktitle: {dir_title}  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: {compute_dir_weight(dir_prefix)} # Position in the left sidebar
# ============================================================

# ========== Basic metadata ==========
title: {dir_title}
date: {datetime.now().strftime('%Y-%m-%d')}
draft: false
authors:
  - admin
tags:
  - {dir_tag}
  - {parent_tag}
categories:
  - {parent_tag}
toc: true # Show table of contents
# ====================================

# ========== Advanced metadata =========
profile: false  # Show author profile?
reading_time: true # Show estimated reading time?
share: true  # Show social sharing links?
featured: true
comments: true  # Show comments?
disable_comment: false
---
"""
            )

    for filename in filenames:
        # Extract the prefix and name from the filename
        file_match = re.match(r"^m([0-9]+)_(.*)", filename)
        if not file_match:
            print(f"Error: Invalid filename format for {filename}")
            continue

        file_prefix = int(file_match.group(1))
        file_name = file_match.group(2)

        # Convert filename to title case
        file_title = to_title_case(file_name)

        # Compute weight for the new markdown file
        file_count = len(list(target_dir.glob("*.md")))
        file_weight = compute_weight(dir_prefix, file_count)

        # Create the new markdown file with frontmatter
        with open(target_dir / f"{filename}.md", "w") as f:
            f.write(
                f"""---
# ===== Title, summary, and position in the left sidebar =====
linktitle: {file_title}  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: {file_weight} # Position in the left sidebar
# ============================================================

# ========== Basic metadata ==========
title: {file_title}
date: {datetime.now().strftime('%Y-%m-%d')}
draft: false
authors:
  - admin
tags:
  - {dir_tag}
  - {parent_tag}
categories:
  - {parent_tag}
toc: true # Show table of contents
# ====================================

# ========== Advanced metadata =========
profile: false  # Show author profile?
reading_time: true # Show estimated reading time?
share: true  # Show social sharing links?
featured: true
comments: true  # Show comments?
disable_comment: false
---
"""
            )

        print(f"Markdown file {target_dir / f'{filename}.md'} created successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a markdown file with frontmatter.")
    parser.add_argument("target_directory", help="The target directory path")
    parser.add_argument("filenames", nargs="+", help="The filenames for the markdown files")

    args = parser.parse_args()

    main(args.target_directory, args.filenames)
