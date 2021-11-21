#Importation des packages qu'on va utiliser:
import tkinter as tk
from djitellopy import Tello

 = Tello()    #création d'une instance tello virtuelle
.connect()    #connexion au drone Tello



 = tk.Tk()     #Création d'une fenêtre
.geometry("")   #les dimensions d'hauteur et largeur de la fenêtre
.title("")   #Nom de la fenêtre

battery = .get_battery()     #état de la batterie du drone

#Fonctions Tello :
#Voler en Haut:
def Up() :
    global battery
    print(battery)
    batteryL= tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.move_up()
#Voler en Bas:
def Down() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.move_down()
#Voler à gauche:
def Left() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.move_left()
#Voler à droite:
def Right() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.move_right()
#Voler en Avant:
def Forward() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.move_forward()
#Voler en Arrière:
def Back() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.move_back()
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
= tk.PhotoImage(file="").subsample(8, 8)
 = tk.PhotoImage(file="").subsample(8, 8)
 = tk.PhotoImage(file="").subsample(8, 8)
 = tk.PhotoImage(file="").subsample(8, 8)
 = tk.PhotoImage(file="").subsample(8, 8)
 = tk.PhotoImage(file="").subsample(8, 8)
 = tk.PhotoImage(file="").subsample(8, 8)
 = tk.PhotoImage(file="").subsample(8, 8)
 = tk.PhotoImage(file="").subsample(8, 8)
 = tk.PhotoImage(file="").subsample(8, 8)

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
.mainloop()