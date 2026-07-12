"""
Sanket AI Studio
Logger Module
Version : 1.0
"""

from datetime import datetime


def log(message):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] {message}")
