# sorting_a_download_folder_py
Download Folder Sorter

A Python script that automatically organizes files in your Downloads (or Desktop) folder by file type. 
The script monitors a specified folder (e.g., D:\Download Folder) and automatically moves files into subfolders based on their file extensions (e.g., PDF, Word, Excel, Images, Games, ZIP files).

Features
Automatically sorts files into designated folders based on file extension.
Real-time monitoring of new or modified files using the watchdog library.
Works for both Windows and Mac systems with customizable download or desktop directory paths.
Requirements
Python 3.x
watchdog library for file monitoring:
bash
Copy code
pip install watchdog
Folder Structure
The script creates the following folders within the specified directory (e.g., D:\Download Folder):


Word: .doc, .docx
Excel: .xls, .xlsx
PDF: .pdf
Images: .jpg, .jpeg, .png, .gif
Games: .exe, .msi
ZIP: .zip, .rar
Other: Files with any other extensions


SETUP AND USAGE
Download the Script: Save the Python script file as desktop_folder_sorter.py.

Update the Download Directory: In the script, update the path DOWNLOAD_DIR to the folder you want to monitor:


python
Copy code
DOWNLOAD_DIR = Path("D:/Download Folder")  # Set to your custom folder

Run the Script: Open a terminal or command prompt, navigate to the folder where you saved desktop_folder_sorter.py, and execute:


bash
Copy code
python desktop_folder_sorter.py
Continuous Monitoring: The script will initially sort existing files and then continue monitoring the specified folder for any new or modified files.

Stop the Script: To stop monitoring, press Ctrl+C in the terminal where the script is running.

Customization
You can add or remove file types by modifying the EXTENSIONS dictionary in the script:

python

Copy code:

EXTENSIONS = {
    'Word': ['.doc', '.docx'],
    'Excel': ['.xls', '.xlsx'],
    'PDF': ['.pdf'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Games': ['.exe', '.msi'],
    'ZIP': ['.zip', '.rar'],
    'Other': []
}

Troubleshooting:

Files Not Moving? Ensure the watchdog library is installed. Run pip install watchdog if necessary.

Wrong Folder? Make sure file extensions are accurately listed under the desired category in EXTENSIONS.
