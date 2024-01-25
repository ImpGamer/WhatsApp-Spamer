#Importamos las libreias a utilizar, pyautogui y time para pausar y realizar automatizaciones
import pyautogui as pg #pg declarada como variable directa de pyautogui
import time

time.sleep(6) #funcion que espera 6 segundos hasta que la aplicacion se ejecute

#bucle que mandara imprimira los mensajes y los mandara automaticamente
for i in range(50):
    pg.write("Has sido hackeado")
    pg.press('enter')
    time.sleep(0)