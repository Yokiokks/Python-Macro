import keyboard
import time
tecla = input('tecla:')
tempo = int(input('demora:'))
while True:
     keyboard.press(tecla)
     time.sleep(tempo)
     print(F"tecla pressionada '{tecla}'")



