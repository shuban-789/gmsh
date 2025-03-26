import pyautogui
import time
import subprocess
import threading
import sys
import os
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener, Key

# BINDINGS
sleep = lambda t: time.sleep(t)
moveTo = lambda a1, a2, t: pyautogui.moveTo(a1, a2, duration=t)
click = lambda a1, a2: pyautogui.click(a1, a2)
scroll = lambda a1, a2, a3: pyautogui.scroll(a1, a2, a3)
write = lambda a1: pyautogui.write(a1)

mouse_actions = []
keyboard_actions = []
recording = False

class sigcolors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'
    
def get_active_window():
    try:
        window_name = subprocess.check_output(["xdotool", "getactivewindow", "getwindowname"], encoding='utf-8')
        return window_name.strip()
    except subprocess.CalledProcessError:
        return None

def is_gmsh_active():
    return get_active_window() and "Gmsh" in get_active_window()

def on_move(x, y):
    if recording and is_gmsh_active():
        mouse_actions.append(('move', x, y))

def on_click(x, y, button, pressed):
    if recording and pressed and is_gmsh_active():
        mouse_actions.append(('click', x, y))

def on_scroll(x, y, dx, dy):
    if recording and is_gmsh_active():
        mouse_actions.append(('scroll', x, y, dx, dy))

def on_press(key):
    if key == Key.esc:
        return False

def on_release(key):
    pass

def start_listeners():
    with MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mouse_listener, \
         KeyboardListener(on_press=on_press, on_release=on_release) as keyboard_listener:
        mouse_listener.join()
        keyboard_listener.join()

def generate_replay_script():
    script = '''
import pyautogui
import time
import subprocess

sleep = lambda t: time.sleep(t)
moveTo = lambda a1, a2, t: pyautogui.moveTo(a1, a2, duration=t)
click = lambda a1, a2: pyautogui.click(a1, a2)
scroll = lambda a1, a2, a3: pyautogui.scroll(a1, a2, a3)
write = lambda a1: pyautogui.write(a1)

subprocess.Popen(["gmsh"])

sleep(5)

'''
    
    for action in mouse_actions:
        if action[0] == 'move':
            script += f"moveTo({action[1]}, {action[2]}, 0.1)\n"
        elif action[0] == 'click':
            script += f"click({action[1]}, {action[2]})\n"
        elif action[0] == 'scroll':
            script += f"scroll({action[3]}, {action[1]}, {action[2]})\n"
    
    for action in keyboard_actions:
        if action[0] == 'press':
            script += f"write('{action[1]}')\n"

    script += '''
# END OF REPLAY SCRIPT
'''

    with open("replay.py", "w") as f:
        f.write(script)
    print("Replay script generated as 'replay_gmsh.py'.")

def track_and_replay():
    global recording
    print("Monitoring for Gmsh...")

    while True:
        if is_gmsh_active() and not recording:
            print(sigcolors.GREEN + ">>" + sigcolors.END + " Gmsh instance detected. Starting recording...")
            recording = True
            listener_thread = threading.Thread(target=start_listeners)
            listener_thread.start()

        if not is_gmsh_active() and recording:
            print(sigcolors.RED + "<<" + sigcolors.END + " Gmsh instance closed. Stopping recording...")
            recording = False
            generate_replay_script()
            break

        sleep(1)

    print("Recording finished. Replay script generated.")

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "record":
            track_and_replay()
        elif sys.argv[1] == "clean":
            os.remove("replay.py")
        else:
            print("Usage: python3 macro.py [record|clean]")
    else:
        print("Usage: python3 macro.py [record|clean]")

if __name__ == "__main__":
    main()
