import os
import sys
from pathlib import Path

def check_environment():
    print("Current working directory:", os.getcwd())
    print("\nPython path:")
    for path in sys.path:
        print(f"  - {path}")
    
    print("\nProject structure:")
    project_root = Path(__file__).parent
    for path in project_root.rglob("*"):
        if path.is_file():
            print(f"  - {path.relative_to(project_root)}")

if __name__ == "__main__":
    check_environment()