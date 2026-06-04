# ============================================================
#  FILE ORGANIZER SCRIPT
#  Author  : Dhanyashree Sen
#  College : JK Lakshmipat University
#  Project : Vacation Project 3 — Automation with Python
# ============================================================

import os
import shutil

# ------------------------------------------------------------------
# STEP 1 — Define where each file extension should go
# ------------------------------------------------------------------
# This dictionary maps a folder name → list of file extensions.
# When the script finds a file, it checks this dictionary to decide
# which folder to move it into.
# ------------------------------------------------------------------

FOLDER_MAP = {
    "Images":     [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"],
    "Videos":     [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"],
    "Audio":      [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Documents":  [".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf", ".md"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods"],
    "Presentations": [".ppt", ".pptx", ".odp"],
    "Code":       [".py", ".c", ".cpp", ".js", ".html", ".css", ".java", ".ts", ".json", ".xml", ".sh"],
    "Archives":   [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"],
    "Executables": [".exe", ".msi", ".apk", ".dmg"],
    "Others":     []   # catch-all for anything not listed above
}


# ------------------------------------------------------------------
# STEP 2 — Helper function: figure out which folder a file belongs to
# ------------------------------------------------------------------

def get_destination_folder(filename):
    """
    Given a filename like 'photo.jpg', return the folder it belongs to.
    Example: 'photo.jpg'  → 'Images'
             'resume.pdf' → 'Documents'
             'weird.xyz'  → 'Others'
    """
    # os.path.splitext splits 'photo.jpg' into ('photo', '.jpg')
    _, extension = os.path.splitext(filename)
    extension = extension.lower()   # make it lowercase so .JPG == .jpg

    for folder_name, extensions in FOLDER_MAP.items():
        if extension in extensions:
            return folder_name

    return "Others"   # nothing matched → put in Others


# ------------------------------------------------------------------
# STEP 3 — Core function: scan folder and move files
# ------------------------------------------------------------------

def organize_folder(target_path):
    """
    Scans the given folder, creates subfolders as needed,
    and moves every file into the right subfolder.
    """

    # --- Safety check: does the folder actually exist? ---
    if not os.path.exists(target_path):
        print(f"  ERROR: The folder '{target_path}' does not exist.")
        print("  Please check the path and try again.")
        return

    print(f"\n{'='*55}")
    print(f"  FILE ORGANIZER — by Dhanyashree Sen")
    print(f"{'='*55}")
    print(f"  Scanning: {target_path}\n")

    # Counters so we can show a summary at the end
    moved_count  = 0
    skip_count   = 0
    error_count  = 0

    # os.listdir() gives us every file AND folder name inside target_path
    all_items = os.listdir(target_path)

    for item_name in all_items:

        # Build the full path, e.g. C:/Users/Dhanya/Downloads/photo.jpg
        item_full_path = os.path.join(target_path, item_name)

        # ---- Skip if it's a folder (we only move files) ----
        if os.path.isdir(item_full_path):
            print(f"  [SKIP]  '{item_name}'  — it's a folder, skipping.")
            skip_count += 1
            continue

        # ---- Decide destination ----
        destination_folder_name = get_destination_folder(item_name)
        destination_folder_path = os.path.join(target_path, destination_folder_name)

        # ---- Create the subfolder if it doesn't exist yet ----
        os.makedirs(destination_folder_path, exist_ok=True)

        # ---- Handle name conflict: if a file with same name already
        #      exists in destination, add a number to the end ----
        destination_file_path = os.path.join(destination_folder_path, item_name)

        if os.path.exists(destination_file_path):
            base, ext = os.path.splitext(item_name)
            counter = 1
            while os.path.exists(destination_file_path):
                new_name = f"{base}_{counter}{ext}"
                destination_file_path = os.path.join(destination_folder_path, new_name)
                counter += 1

        # ---- Actually move the file ----
        try:
            shutil.move(item_full_path, destination_file_path)
            print(f"  [MOVED] '{item_name}'  →  {destination_folder_name}/")
            moved_count += 1
        except Exception as e:
            print(f"  [ERROR] Could not move '{item_name}': {e}")
            error_count += 1

    # ---- Print summary ----
    print(f"\n{'='*55}")
    print(f"  DONE! Summary:")
    print(f"    Files moved  : {moved_count}")
    print(f"    Skipped      : {skip_count}")
    print(f"    Errors       : {error_count}")
    print(f"{'='*55}\n")


# ------------------------------------------------------------------
# STEP 4 — Entry point: ask the user which folder to organize
# ------------------------------------------------------------------

if __name__ == "__main__":
    print("\n  Welcome to the File Organizer!")
    print("  (Press Ctrl+C at any time to cancel)\n")

    # Ask the user to type the folder path they want to organize
    folder_path = input("  Enter the full path of the folder to organize:\n  > ").strip()

    # Remove quotes if the user copy-pasted a path with quotes
    folder_path = folder_path.strip('"').strip("'")

    organize_folder(folder_path)
