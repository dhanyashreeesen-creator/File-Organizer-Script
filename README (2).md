# 📁 File Organizer Script

> A Python automation script that sorts a messy folder into clean subfolders — automatically.

**Author:** Dhanyashree Sen  
**College:** JK Lakshmipat University  
**Year:** 1st Year Engineering (CS)  
**Built during:** Summer Vacation Project

---

## 🚀 What Does It Do?

You know that Downloads folder that has 300 random files — photos, PDFs, ZIPs, videos — all dumped in one place?

This script fixes that. You run it, point it at any folder, and it **automatically sorts every file** into labeled subfolders like:

```
📂 YourFolder/
├── 📁 Images/        ← all .jpg, .png, .gif ...
├── 📁 Documents/     ← all .pdf, .docx, .txt ...
├── 📁 Videos/        ← all .mp4, .mkv ...
├── 📁 Audio/         ← all .mp3, .wav ...
├── 📁 Code/          ← all .py, .c, .html ...
├── 📁 Spreadsheets/  ← all .xlsx, .csv ...
├── 📁 Archives/      ← all .zip, .rar ...
└── 📁 Others/        ← anything else
```

---

## 🛠️ Technologies Used

- **Python 3** — core language
- `os` module — for reading folders and file paths
- `shutil` module — for moving files
- No pip installs needed — runs on plain Python!

---

## ▶️ How to Run

**Step 1:** Make sure Python 3 is installed  
```
python --version
```

**Step 2:** Download or clone this repository
```
git clone https://github.com/YOUR_USERNAME/file-organizer.git
cd file-organizer
```

**Step 3:** Run the script
```
python organizer.py
```

**Step 4:** When prompted, paste the path to the folder you want to organize
```
Enter the full path of the folder to organize:
> C:\Users\Dhanya\Downloads
```

That's it. Watch it sort everything automatically!

---

## 💡 Example Output

```
=======================================================
  FILE ORGANIZER — by Dhanyashree Sen
=======================================================
  Scanning: C:\Users\Dhanya\Downloads

  [MOVED] 'photo1.jpg'         →  Images/
  [MOVED] 'resume.pdf'         →  Documents/
  [MOVED] 'song.mp3'           →  Audio/
  [MOVED] 'project.zip'        →  Archives/
  [MOVED] 'notes.py'           →  Code/
  [SKIP]  'Old Projects'       — it's a folder, skipping.

=======================================================
  DONE! Summary:
    Files moved  : 5
    Skipped      : 1
    Errors       : 0
=======================================================
```

---

## 📂 Supported File Types

| Folder        | Extensions |
|---------------|-----------|
| Images        | .jpg .jpeg .png .gif .bmp .svg .webp |
| Videos        | .mp4 .mkv .avi .mov .wmv .flv |
| Audio         | .mp3 .wav .aac .flac .ogg .m4a |
| Documents     | .pdf .doc .docx .txt .md .rtf |
| Spreadsheets  | .xls .xlsx .csv .ods |
| Presentations | .ppt .pptx .odp |
| Code          | .py .c .cpp .js .html .css .java |
| Archives      | .zip .rar .tar .gz .7z |
| Executables   | .exe .msi .apk .dmg |
| Others        | Anything not listed above |

---

## 🧠 What I Learned Building This

- How to use `os.listdir()` to read a folder's contents
- How to use `os.path.splitext()` to get a file's extension
- How `shutil.move()` works to relocate files
- How to handle edge cases (duplicate filenames, permission errors)
- How to structure Python code with functions
- How to write clean, commented code

---

## 🔮 Possible Future Improvements

- [ ] Add a GUI using Tkinter so users can browse for folders visually
- [ ] Add an "undo" feature to reverse the organization
- [ ] Sort files by date modified instead of type
- [ ] Send an email/notification summary after organizing
- [ ] Schedule it to run automatically every week

---

## 📄 License

This project is open source and free to use.

---

*Built with Python 🐍 during summer vacation — first real project!*
