import keyboard
import time

def press_space(interval):
    while True:
        keyboard.press('w')
        time.sleep(interval)
        keyboard.release('w')
        time.sleep(interval)

press_w(0.1)

