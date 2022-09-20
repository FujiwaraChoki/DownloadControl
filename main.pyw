import os.path
from os import listdir
from os.path import isfile, join
import shutil

"""
@author: Sami Hindi
@email: sami@samihindi.com
@website: https://samihindi.com
@date: 20.09.2022 (EU)
@version: 0.0.1
@description: This script is used to sort files in a directory into different folders based on their file extension.
@license: MIT
"""


# Function to only return files from a certain directory
def files_in_dir(directory: str):
    if os.path.isdir(directory):
        return [f for f in listdir(directory) if isfile(join(directory, f))]
    else:
        return None


if __name__ == "__main__":
    files = files_in_dir("C:\\Users\\Sami\\Downloads")
    if files is None:
        print("Directory does not exist.")
        exit(0)
    for file in files:
        if file.endswith((".mp4" or ".mkv" or ".mov" or ".webm" or ".avi")):
            shutil.move("C:\\Users\\Sami\\Downloads\\" + file, "D:\\Downloads\\Videos\\" + file)
        elif file.endswith((".jpg" or ".png" or ".jpeg" or ".gif" or ".bmp")):
            shutil.move("C:\\Users\\Sami\\Downloads\\" + file, "D:\\Downloads\\Images\\" + file)
        elif file.endswith((".mp3" or ".wav" or ".ogg" or ".flac" or ".m4a")):
            shutil.move("C:\\Users\\Sami\\Downloads\\" + file, "D:\\Downloads\\Music\\" + file)
        elif file.endswith((".pdf" or ".doc" or ".docx" or ".txt" or ".rtf")):
            shutil.move("C:\\Users\\Sami\\Downloads\\" + file, "D:\\Downloads\\Documents\\" + file)
        elif file.endswith((".zip" or ".rar" or ".7z" or ".tar" or ".gz")):
            shutil.move("C:\\Users\\Sami\\Downloads\\" + file, "D:\\Downloads\\Archives\\" + file)
        elif file.endswith((".exe" or ".msi" or ".bat" or ".cmd" or ".sh")):
            shutil.move("C:\\Users\\Sami\\Downloads\\" + file, "D:\\Downloads\\Binaries\\" + file)
        else:
            shutil.move("C:\\Users\\Sami\\Downloads\\" + file, "D:\\Downloads\\Other\\" + file)