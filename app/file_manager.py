"""
Sanket AI Studio
File Manager
Version : 1.0
"""

import os


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"📁 Created : {folder_path}")
    else:
        print(f"✅ Exists : {folder_path}")


def file_exists(file_path):
    return os.path.exists(file_path)
