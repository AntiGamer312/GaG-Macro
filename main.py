import pyautogui
from time import sleep
from functions import utils

#Poses for seeds buttons: (625, 435), (625, 565) 23 fruits
#Can buy colours, (29, 179, 29)

def main():
    sleep(5)
    pos = (625, 435)

    utils.cycle_shop(pos, 23)

if __name__ == "__main__":
    main()