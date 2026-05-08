# File Organizer Automation

A professional Python automation tool that automatically organizes files into folders based on file type.

---

## Features

- Automatically sorts files
- Creates folders dynamically
- Supports dry-run mode
- Logs actions
- Clean CLI interface

---

## Technologies Used

- Python 3
- pathlib
- shutil
- argparse
- logging

---

## Usage

### Dry Run

```bash
python organizer.py sample_files --dry-run
```

### Actual Run

```bash
python organizer.py sample_files
```

---

## Example Output

```text
[MOVED] photo.jpg --> Images/
[MOVED] resume.pdf --> Documents/
```

---

## Future Improvements

- GUI version
- Duplicate handling
- Undo feature
- AI classification

---

## License

MIT