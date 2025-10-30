import keyboard
import time
tecla = input("Insira a sua tecla:")
tempo = input("tempo de demora:")
def press_space():
    while True:
        keyboard.press(tecla)
        time.sleep(tempo)
        print("tecla pressionada", tecla)
press_space()



