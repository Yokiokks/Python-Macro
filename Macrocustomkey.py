import keyboard
import time

def macro():
    while True:
        time.sleep(0.1)
        keyboard.send("w") 
        print("Tecla pressionada")

macro()

