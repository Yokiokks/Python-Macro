import keyboard
import time

def macro():
    while True:
        time.sleep(0.1)  # Espera por 60 segundos (1 minuto)
        keyboard.send("w")  # Simula o pressionamento da tecla 'espaço'
        print("Tecla pressionada")

# Para iniciar a macro, basta executar a função macro
macro()
