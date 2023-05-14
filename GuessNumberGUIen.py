import tkinter as tk
from tkinter import *
import random

def Check_ans(event):   #Function to check player answers with random number generated by computer
    global player_attempt, information, attempts
    player_try = int(player_attempt.get())

    attempts = attempts - 1
    player_attempt.delete(0, END)

    if player_try == ans:
        string_variable.set(f"Congratulation, this is correct number.\n{attempts} attempts left. Click New Game button or n key to start new game.")
        Button_Check.pack_forget()

    elif attempts == 0:
        string_variable.set(f"Unfortunatelly you are out of attempts. \nYou were looking for a number: {ans}")
        Button_Check.pack_forget()

    elif player_try < ans:
        string_variable.set(f"Wrong number. {attempts} attempts left. \nTry with higher number.")

    elif player_try > ans:
        string_variable.set(f"Wrong number. {attempts} attempts left. \nTry lower number.")

def StartGame(event):   #function to start new game
    global attempts, ans
    attempts = 10
    ans = random.randint(1,99)
    string_variable.set("New game. You have 10 attempts.")
    player_attempt.place(x=270, y=90)
    player_attempt.focus_set()
    player_attempt.delete(0, END)
    Button_Check.place(x=340, y=150)

def ExitGame(event):    #function to close window 
    my_window.destroy()


#create the window
my_window = tk.Tk()
my_window.geometry("750x200")
my_window.title("Guess The Number")

#opis gry
purpose = tk.Label(my_window, text="Guess the number between 1 & 99. You have got 10 attempts. Good luck!!", borderwidth=3, font=('Times New Roman', 16, 'bold'))
purpose.pack()

#okienko wpisywania odpowiedzi
player_attempt = tk.Entry(my_window, width=30, borderwidth=7)
player_attempt.pack_forget()

#Okienko informacji
string_variable = tk.StringVar(my_window, "Click New Game button or key n to start.")
information = tk.Label(my_window, textvariable=string_variable, font=('Times New Roman', 16, 'bold'))
information.pack()

#przycisk sprawdzania
Button_Check = tk.Button(my_window, text="Check", command=Check_ans)
Button_Check.pack_forget()
my_window.bind('<Return>', Check_ans) #Return to submit player answer

#przycisk nowej gry
New_Game = tk.Button(my_window, text="New Game", command=StartGame)
New_Game.pack(side=RIGHT)
my_window.bind('<Key-n>', StartGame) #Key 'n' to Start new game

#przycisk wyjścia
Button_Quit = tk.Button(my_window, text="Quit", command=my_window.destroy)
Button_Quit.pack(side=LEFT)
my_window.bind('<Escape>', ExitGame) #Escape key to close the window


my_window.mainloop()