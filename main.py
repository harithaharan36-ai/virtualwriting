import tkinter as tk
from src.gui import AirWritingApp
from src.logger import logger
import sys

def main():
    try:
        root = tk.Tk()
        app = AirWritingApp(root)
        root.protocol("WM_DELETE_WINDOW", app.on_closing)
        logger.info("Application started.")
        root.mainloop()
    except Exception as e:
        logger.critical(f"Application failed to start: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
