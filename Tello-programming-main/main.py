#Importation des packages qu'on va utiliser:
import tkinter as tk
from djitellopy import Tello

kn = Tello()    #création d'une instance tello virtuelle
kn.connect()    #connexion au drone Tello



window = tk.Tk()     #Création d'une fenêtre
window.geometry("650x400")   #les dimensions d'hauteur et largeur de la fenêtre
window.title("Tello Controller")   #Nom de la fenêtre

battery = kn.get_battery()     #état de la batterie du drone

#Fonctions Tello :
#Voler en Haut:
def Up() :
    global battery
    print(battery)
    batteryL= tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.move_up(30)
#Voler en Bas:
def Down() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.move_down(30)
#Voler à gauche:
def Left() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.move_left(50)
#Voler à droite:
def Right() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.move_right(50)
#Voler en Avant:
def Forward() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.move_forward(50)
#Voler en Arrière:
def Back() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.move_back(50)
#Décoller
def takeoff():
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.takeoff()
#Atterir
def land() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.land()
#Flip gauche:
def flipL() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.flip_left()
#Flip droit:
def flipR() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.flip_right()


#Importation des images png:
imgUp = tk.PhotoImage(file="up.png").subsample(8, 8)
imgDown = tk.PhotoImage(file="down.png").subsample(8, 8)
imgLeft = tk.PhotoImage(file="left.png").subsample(8, 8)
imgRight = tk.PhotoImage(file="right.png").subsample(8, 8)
imgForward = tk.PhotoImage(file="forward.png").subsample(8, 8)
imgBack = tk.PhotoImage(file="back.png").subsample(8, 8)
imgTakeoff = tk.PhotoImage(file="takeoff.png").subsample(8, 8)
imgLand = tk.PhotoImage(file="land.png").subsample(8, 8)
imgfleft = tk.PhotoImage(file="flipL.png").subsample(8, 8)
imgfright = tk.PhotoImage(file="flipR.png").subsample(8, 8)

#Création et Assignations des boutons:
btnUp = tk.Button(image=imgUp, command=Up)
btnUp.grid(row=1, column=2, pady=10, padx=10)

btnDown = tk.Button(image=imgDown, command=Down)
btnDown.grid(row=3, column=2, pady=10, padx=10)

btnLeft = tk.Button(image=imgLeft, command=Left)
btnLeft.grid(row=2, column=1, pady=10, padx=10)

btnRight = tk.Button(image=imgRight, command=Right)
btnRight.grid(row=2, column=3, pady=10, padx=10)

btnForward = tk.Button(image=imgForward, command=Forward)
btnForward.grid(row=0, column=0, pady=10, padx=10)

btnBack = tk.Button(image=imgBack, command=Back)
btnBack.grid(row=1, column=0, pady=10, padx=10)

btntakeoff = tk.Button(image=imgTakeoff, command=takeoff)
btntakeoff.grid(row=0, column=4, pady=10, padx=10)

btnland = tk.Button(image=imgLand, command=land)
btnland.grid(row=1, column=4, pady=10, padx=10)

btnFleft = tk.Button(image=imgfleft, command=flipL)
btnFleft.grid(row=2, column=5, pady=10, padx=10)

btnFright = tk.Button(image=imgfright, command=flipR)
btnFright.grid(row=2, column=6, pady=10, padx=10)


#Cette fonction de boucle doit toujours être executée en dernier:
window.mainloop()
