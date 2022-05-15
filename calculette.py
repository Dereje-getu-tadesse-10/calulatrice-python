import re
from time import sleep
from turtle import clear
from os import system

# function calcule


def calcule():
    wel = "Hello"
    print(wel)
    sleep(1)
    print("Quelle operation veux tu effectuer ?")
    sleep(1)
    addition = print("1 Addition")
    sleep(1)
    soustraction = print("2 Soustraction")
    sleep(1)
    multiplication = print("3 Multiplication")
    sleep(1)
    division = print("4 Division")
    choice = input('votre choix : ')
    choice = int(choice)
    # addition
    if choice == 1:
        print("vous avez choisie de faire une addition")
        choice1 = input("votre premier calcule : ")
        choice2 = input("votre premier calcule : ")
        choice1 = int(choice1)
        choice2 = int(choice2)
        print(choice1 + choice2)
    # soustraction
    elif choice == 2:
        print("vous avez choisie de faire une soustraction")
        choice1 = input("votre premier calcule : ")
        choice2 = input("votre premier calcule : ")
        choice1 = int(choice1)
        choice2 = int(choice2)
        print(choice1 - choice2)
    # multiplication
    elif choice == 3:
        print("vous avez choisie de faire une multiplication")
        choice1 = input("votre premier calcule : ")
        choice2 = input("votre premier calcule : ")
        choice1 = int(choice1)
        choice2 = int(choice2)
        print(choice1 * choice2)
    # division
    elif choice == 4:
        print("vous avez choisie de faire une division")
        choice1 = input("votre premier calcule : ")
        choice2 = input("votre premier calcule : ")
        choice1 = int(choice1)
        choice2 = int(choice2)
        print(choice1 - choice2)
    # condition si le choix et inferieur a 0 ou si il et superieru a 4
    if choice <= 0 or choice > 4:
        # Clear de la console (terminal)
        _ = system('clear')
        print('Choix valide entre 1 et 4')
        return calcule()

calcule()
