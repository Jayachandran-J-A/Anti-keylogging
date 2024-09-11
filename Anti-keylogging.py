import os
import re
from tqdm import tqdm  # Import tqdm for the progress bar

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

if __name__ == "__main__":
    # Adjust the root_folder to the desired starting point for the file search
    root_folder = r"C:\Users\jayac\Anti-Keylog-Test"  

    all_files = scan_files(root_folder)

    # Integrate tqdm for a progress bar
    for file_path in tqdm(all_files, desc="Scanning Files", unit="file"):
        detect_and_remove_keylogger(file_path)
