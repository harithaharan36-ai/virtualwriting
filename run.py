import os
import subprocess
import sys

def check_dependencies():
    try:
        import cv2
        import mediapipe
        import easyocr
        return True
    except ImportError:
        return False

if __name__ == "__main__":
    if not check_dependencies():
        print("Dependencies missing. Installing from requirements.txt...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    print("Launching Virtual Air Writing AI...")
    from main import main
    main()
