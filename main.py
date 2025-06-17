import pyautogui
import keyboard

print(pyautogui.size())

def get_values():

    pos = pyautogui.position()
    print(pos, pyautogui.pixel(pos))

keyboard.add_hotkey("q", get_values())

keyboard.wait("esc")