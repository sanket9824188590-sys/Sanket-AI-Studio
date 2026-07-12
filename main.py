"""
Sanket AI Studio
Main Application
Version : 1.0
"""

from app.logger import log
from app.validator import validate_project
from app.file_manager import create_folder

PROJECT_DIR = "."


def main():
    log("🚀 Starting Sanket AI Studio...")

    create_folder("logs")
    create_folder("temp")
    create_folder("cache")

    validate_project(PROJECT_DIR)

    log("✅ Initialization Complete.")


if __name__ == "__main__":
    main()
