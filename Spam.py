import pyautogui as pt  #Pip install pyautogui  
import time 

limit =  input("cantidad de mensajes: ")
message = input("mensaje: ")
i = 0

time.sleep(3)

while i < int(limit):
    pt.typewrite(message)
    pt.press("enter")

    i += 1
