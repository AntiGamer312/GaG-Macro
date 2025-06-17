import pyautogui as pag

offset = 5.2

class utils():

    #Buys all the items in a shop
    def cycle_shop(start_pos : tuple, items : int):

        for item in range(items):

            #Clicks the fruit
            pag.moveTo(start_pos[0], (start_pos[1] * (item * offset) + 50))
            pag.click()

            #Buys the fruit
            pag.moveTo(start_pos[0], (start_pos[1] * (item * offset)))
            pag.click()

            #Removes the buy option
            pag.moveTo(start_pos[0], (start_pos[1] * (item * offset) + 50))
            pag.click()
