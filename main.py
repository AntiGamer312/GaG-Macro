import pyautogui
import keyboard

#Poses for seeds buttons: (630, 430), (630, 560)
#Can buy colours, (29, 179, 29)

print(pyautogui.size())

def get_values():

    pos = pyautogui.position()
    print(pos, pyautogui.pixel(pos[0], pos[1]))

keyboard.add_hotkey("q", get_values)

keyboard.wait("esc")