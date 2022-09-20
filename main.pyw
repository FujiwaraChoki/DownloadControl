import os.path
from os import listdir
from os.path import isfile, join
import shutil
import time

"""
@author: Sami Hindi
@email: sami@samihindi.com
@website: https://samihindi.com
@date: 20.09.2022 (EU)
@version: 0.0.3
@description: This script is used to sort files in a directory into different folders based on their file extension.
@license: MIT
"""

print("Starting file management...")


def wait():
    time.sleep(3)


# Function to only return files from a certain directory
def files_in_dir(directory: str):
    if os.path.isdir(directory):
        return [f for f in listdir(directory) if isfile(join(directory, f))]
    else:
        return None


# Function which utilizes the files_in_dir function to sort files into different folders based on their file extension
def manage():
    files = files_in_dir("D:\\DDownloads")
    if files is None:
        print("Directory does not exist.")
        exit(0)
    for file in files:
        if file.endswith(".tmp") or file.endswith(".crdownload") or file.endswith(".opdownload"):
            wait()
            continue
        if file.endswith((".mp4" or ".mkv" or ".mov" or ".webm" or ".avi")):
            wait()
            target_dir = "D:\\Downloads\\Videos"
            if ("mylivewallpapers" or "wallpapers" or "wallpaper") in file:
                target_dir = "D:\\Downloads\\Videos\\Wallpapers\\"
            shutil.move("D:\\DDownloads\\" + file, target_dir + file)

        elif file.endswith((".jpg" or ".png" or ".jpeg" or ".gif" or ".bmp")):
            wait()
            shutil.move("D:\\DDownloads\\" + file, "D:\\Downloads\\Images\\" + file)

        elif file.endswith((".mp3" or ".wav" or ".ogg" or ".flac" or ".m4a")):
            wait()
            shutil.move("D:\\DDownloads\\" + file, "D:\\Downloads\\Music\\" + file)

        elif file.endswith((".pdf" or ".doc" or ".docx" or ".txt" or ".rtf")):
            wait()
            shutil.move("D:\\DDownloads\\" + file, "D:\\Downloads\\Documents\\" + file)

        elif file.endswith((".zip" or ".rar" or ".7z" or ".tar" or ".gz")):
            wait()
            shutil.move("D:\\DDownloads\\" + file, "D:\\Downloads\\Archives\\" + file)

        elif file.endswith((".exe" or ".msi" or ".bat" or ".cmd" or ".sh")):
            wait()
            shutil.move("D:\\DDownloads\\" + file, "D:\\Downloads\\Binaries\\" + file)

        else:
            wait()
            shutil.move("D:\\DDownloads\\" + file, "D:\\Downloads\\Other\\" + file)


# Main
try:
    while True:
        manage()
except KeyboardInterrupt:
    print("Exiting...")
    exit(0)
except Exception as error:
    print(f"An error has occurred: {error}")
