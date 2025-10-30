import keyboard
import time

def press_space(interval):
    while True:
        keyboard.press("YOURKEYHERE")
        time.sleep(interval)
press_space(0.1)


