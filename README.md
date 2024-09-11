# Anti-Keylogging and Keylogging Programs

This project consists of an anti-keylogging tool and various keylogging programs developed for testing and demonstration purposes. The anti-keylogging script scans files and removes any that match predefined keylogger patterns, while the keylogging programs are designed to capture and log keystrokes.

## Table of Contents
- [Project Structure](#project-structure)
- [Anti-Keylogging Tool](#anti-keylogging-tool)
  - [Features](#features)
  - [Usage](#usage)
- [Keylogging Programs](#keylogging-programs)
  - [Keylogger (C++)](#keylogger-c)
  - [Process Monitor (Python)](#process-monitor-python)
  - [Startup Scripts](#startup-scripts)
- [How to Run](#how-to-run)
- [Disclaimer](#disclaimer)

## Project Structure
- **Anti-keylogging.py**: A Python program that detects and removes keyloggers by scanning files for specific patterns.
- **klog_main.exe**: A C++ keylogger program that logs keystrokes to a file.
- **monitor.py**: A Python script that monitors running processes and triggers the keylogger when a target process is detected.
- **pressed_keys.txt**: A log file for storing keystrokes.
- **startup.bat** & **startup2.bat.lnk**: Batch scripts for automating the startup of the keylogger monitor.

## Anti-Keylogging Tool

### Features
- Scans directories for files containing suspicious keylogger patterns.
- Automatically deletes files that match predefined keylogger patterns.
- Progress bar with real-time feedback on the scanning process.

### Usage
1. Run `Anti-keylogging.py`.
2. Select the directory you want to scan.
3. The tool will display a message for each file scanned and indicate whether a keylogger was found and removed.

## Keylogging Programs

### Keylogger (C++)
- **klog_main.exe** captures keystrokes and logs them to a file.
- Configurable options to change logging format (e.g., ASCII, hexadecimal).
- Logs special keys (e.g., Backspace, Shift) with descriptive tags.

### Process Monitor (Python)
- **monitor.py** monitors for the execution of a specific process (e.g., Notepad.exe).
- When the target process is running, it starts the keylogger automatically.

### Startup Scripts
- **startup.bat**: Script to start the process monitor on system startup.
- **startup2.bat.lnk**: Shortcut to automate execution of the `startup.bat` script.

## How to Run

### Anti-Keylogger:
- Install required libraries: `tkinter`, `tqdm`, `psutil`.
- Run the `Anti-keylogging.py` script from your terminal or Python IDE.

### Keylogger:
1. Compile the C++ keylogger code into an executable (`klog_main.exe`).
2. Optionally, use `monitor.py` to run the keylogger when the target process is detected.

### Startup Scripts:
- Place the `startup.bat` in your startup directory to trigger the monitor on system boot.

## Disclaimer
This project is for educational purposes only. The keylogging programs are designed to demonstrate the functionality of keyloggers and should not be used for malicious activities. Always ensure you have permission to monitor or log keystrokes on any device.
