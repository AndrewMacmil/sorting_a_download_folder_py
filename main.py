import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path

# Define paths
DOWNLOAD_DIR = Path("D:/Download Folder")  # Set to your custom download folder
DESTINATIONS = {
    'Word': DOWNLOAD_DIR / "Word",
    'Excel': DOWNLOAD_DIR / "Excel",
    'PDF': DOWNLOAD_DIR / "PDF",
    'Images': DOWNLOAD_DIR / "Images",
    'Games': DOWNLOAD_DIR / "Games",
    'ZIP': DOWNLOAD_DIR / "ZIP",
    'Other': DOWNLOAD_DIR / "Other"
}

# Define file extensions
EXTENSIONS = {
    'Word': ['.doc', '.docx'],
    'Excel': ['.xls', '.xlsx'],
    'PDF': ['.pdf'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Games': ['.exe', '.msi'],
    'ZIP': ['.zip','.rar'],  # Add ZIP files specifically
    'Other': []
}

# Create target folders if they don't exist
for folder in DESTINATIONS.values():
    folder.mkdir(parents=True, exist_ok=True)

# Function to move a file to the right folder
def move_file(file):
    dest_folder = DESTINATIONS['Other']  # Default to 'Other' if no match
    for folder, extensions in EXTENSIONS.items():
        if file.suffix in extensions:
            dest_folder = DESTINATIONS[folder]
            break
    shutil.move(str(file), dest_folder / file.name)
    print(f"Moved {file.name} to {dest_folder}")

# Initial sorting of all files already in the download folder
def initial_sort():
    for file in DOWNLOAD_DIR.iterdir():
        if file.is_file():
            move_file(file)

# Event handler for monitoring new files
class FileMoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in DOWNLOAD_DIR.iterdir():
            if file.is_file():
                move_file(file)

# Start the observer and perform initial sorting
observer = Observer()
observer.schedule(FileMoverHandler(), DOWNLOAD_DIR, recursive=False)

print("Sorting existing files in the Download folder...")
initial_sort()  # Sort all files in the download folder initially
print("Monitoring Download folder for new files...")

observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()
observer.join()
