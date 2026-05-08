from pathlib import Path
import shutil
import argparse
import logging

# ==============================
# Logging Setup
# ==============================

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ==============================
# File Categories
# ==============================

FILE_GROUPS = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".md"},
    "Videos": {".mp4", ".mkv", ".avi"},
    "Music": {".mp3", ".wav"},
    "Archives": {".zip", ".rar", ".7z"},
    "Code": {".py", ".html", ".css", ".js", ".cpp"}
}

# ==============================
# Category Detection
# ==============================

def get_category(file_path: Path):

    extension = file_path.suffix.lower()

    for category, extensions in FILE_GROUPS.items():

        if extension in extensions:
            return category

    return "Others"

# ==============================
# Main Organizer Function
# ==============================

def organize_folder(folder_path: Path, dry_run=False):

    if not folder_path.exists():
        print(f"[ERROR] Folder does not exist: {folder_path}")
        return

    if not folder_path.is_dir():
        print(f"[ERROR] Not a folder: {folder_path}")
        return

    print("\nStarting File Organizer...\n")

    processed_files = 0

    for item in folder_path.iterdir():

        if item.is_file():

            category = get_category(item)

            target_folder = folder_path / category
            target_folder.mkdir(exist_ok=True)

            target_path = target_folder / item.name

            if dry_run:

                print(f"[DRY RUN] {item.name} --> {category}/")

            else:

                shutil.move(str(item), str(target_path))

                print(f"[MOVED] {item.name} --> {category}/")

                logging.info(f"Moved file: {item.name} to {category}/")

            processed_files += 1

    print(f"\nCompleted Successfully!")
    print(f"Files Processed: {processed_files}")

# ==============================
# CLI Setup
# ==============================

def main():

    parser = argparse.ArgumentParser(
        description="Automatically organize files by file type."
    )

    parser.add_argument(
        "folder",
        help="Folder path to organize"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without moving files"
    )

    args = parser.parse_args()

    folder_path = Path(args.folder)

    organize_folder(folder_path, args.dry_run)

# ==============================
# Entry Point
# ==============================

if __name__ == "__main__":
    main()