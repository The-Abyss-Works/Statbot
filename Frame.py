import os
from platform import system
import qrcode

def Main():
    running:bool = True
    while running:
        print('''********************
welcome to Statbot Ver.0.1 by The Abyss Works
Develloped by @TheAbyssant
*********************''')
        
        print('''####################
Press 1: Create QR
            
Press 2: Exit''')
        
        n = int(input(">__"))
        if n == 1:
            g = input("EnterLink>__")
            img = qrcode.make(g)
            img.show()
            continue
        if n in range(2,10):
            exit()


def Startup():
    if system() == 'Windows':
        os.system('cls')
    elif system() == 'Linux':
        os.system("clear")
    os.system('title QRCode Maker by TAW')
    Main()


Startup()
