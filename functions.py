import pyautogui as pag

pag.PAUSE = 0.1
offset = 5.2

class utils():

    #Buys all the items in a shop
    def cycle_shop(start_pos : tuple, items : int):

        #Relesitcally make the mouse move and jiggle
        pag.move(start_pos[0], start_pos[1])
        pag.click(button="middle")

        pag.scroll(10000)

        for item in range(items):

            #Clicks the fruit
            pag.moveTo(start_pos[0], (start_pos[1] + (item * offset) + 50))
            pag.click()

            #Buys the fruit
            pag.moveTo(start_pos[0], (start_pos[1] + (item * offset)))
            pag.click()

            #Removes the buy option
            pag.moveTo(start_pos[0], (start_pos[1] + (item * offset) + 50))
            pag.click()

            #Scroll down
            pag.scroll(120)
