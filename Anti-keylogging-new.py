import os
import re
import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm
import tkinter.ttk as ttk


def scan_files(root_folder):
    scanned_files = []

    for foldername, _, filenames in os.walk(root_folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            scanned_files.append(file_path)

    return scanned_files

def detect_and_remove_keylogger(file_path):
    keylogger_patterns = [
        r"import\s+logging.*import\s+os.*import\s+platform.*import\s+smtplib",
        r"from\s+pynput\s+import\s+keyboard",
        # Add more keylogger patterns as needed
    ]

    try:
        with open(file_path, 'r') as file:
            content = file.read()

        for pattern in keylogger_patterns:
            if re.search(pattern, content):
                print(f"Keylogger pattern found in {file_path}. Removing...")
                os.remove(file_path)
                break  # Break the loop after the first detection

        else:
            print(f"No keylogger pattern found in {file_path}.")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def start_scan():
    root_folder = filedialog.askdirectory()
    if root_folder:
        all_files = scan_files(root_folder)
        progress_bar['maximum'] = len(all_files)
        
        for file_path in tqdm(all_files, desc="Scanning Files", unit="file"):
            detect_and_remove_keylogger(file_path)
            progress_bar['value'] += 1
            root.update_idletasks()

root = tk.Tk()
root.title("Anti-Keylogger App")

start_button = tk.Button(root, text="Start Scan", command=start_scan)
start_button.pack(pady=10)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

log_area = tk.Text(root, height=10, width=50)
log_area.pack(pady=10)

root.mainloop()
