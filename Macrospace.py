import keyboard
import time

def press_space(interval):
    while True:
        keyboard.press('w')
        time.sleep(interval)
        keyboard.release('w')
        time.sleep(interval)

# Exemplo de uso: pressionar a tecla de espaço a cada 0.1 segundos
press_w(0.1)
