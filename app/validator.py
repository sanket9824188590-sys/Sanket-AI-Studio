"""
Sanket AI Studio
Validator Module
Version : 1.0
"""

import os


def validate_project(project_dir):
    required_items = [
        "assets",
        "models",
        "outputs",
        "scripts",
        "README.md",
        "requirements.txt",
    ]

    print("🔍 Validating Project...")

    missing = []

    for item in required_items:
        path = os.path.join(project_dir, item)

        if os.path.exists(path):
            print(f"✅ {item}")
        else:
            print(f"❌ {item}")
            missing.append(item)

    if missing:
        print("\n⚠ Missing Items:")
        for item in missing:
            print("-", item)
    else:
        print("\n🎉 Project Validation Successful!")
