import pyautogui
from time import sleep

#Poses for seeds buttons: (625, 435), (625, 565) 23 fruits
#Can buy colours, (29, 179, 29)

pyautogui.moveTo(625, 435)


sleep(5)
pos = (630, 435)
offset = 9

for times in range(23):

    pyautogui.moveTo(pos[0], pos[1] + (offset * times))
