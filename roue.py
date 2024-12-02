import tkinter as tk
import random

def changer_couleur():
    couleur = random.choice(["black", "white"])  
    fenetre.config(bg=couleur) 
    label.config(text=f"Couleur choisie : {couleur}", fg="black" if couleur == "white" else "black")  

fenetre = tk.Tk()
fenetre.title("Choix Aléatoire de Couleur")
fenetre.geometry("400x300")  
fenetre.resizable(False, False)  

fenetre.config(bg="white")

label = tk.Label(fenetre, text="Cliquez sur le bouton pour choisir une couleur", 
                 font=("Helvetica", 16, "bold"), bg="white", fg="black")
label.pack(pady=40)

bouton_changer = tk.Button(fenetre, text="Changer la couleur", command=changer_couleur, 
                           font=("Helvetica", 14, "bold"), bg="#797D7F", fg="white", 
                           relief="raised", width=20, height=2, bd=3, activebackground="#424949")
bouton_changer.pack(pady=20)

fenetre.mainloop()

