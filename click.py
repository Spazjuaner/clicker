import time
import random
import pyautogui
import keyboard
from time import sleep
from tkinter import *

delay = .1

window = Tk()

window.title("Zaps")

#functions
def clickstart():
    time.sleep(3)
    
    run = True
    intervalInt = None
    
    try:
        intervalInt = int(txt.get())
    except:
        pass
    
    start = time.time()
    while run == True:
        
        if keyboard.is_pressed('0'):
            run = False
            break
        
        if intervalInt != None:
            if time.time() >= (start + intervalInt):
                pyautogui.click()
                sleep(delay * random() + 1/2 * delay)
                start = time.time()
        else:
            pyautogui.click()


lbl = Label(window, text= "Delay in Seconds")
lbl.grid(column=1, row=0, padx=(75,10))




txt = Entry(window,width=10)
txt.grid(column=1, row=1, padx=(75,10))

window.geometry("250x100") #size of window

btn = Button(window, text="Start Click", command=clickstart, bg="green", fg="lightgreen")
btn.grid(column=1, row=2, padx=(75,10), pady=(10,10)) #padx and y makes space

txt.focus()
window.mainloop()

window.mainloop()