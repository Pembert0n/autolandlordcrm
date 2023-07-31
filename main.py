"""
tkinter zum erstellen des Fensters
os zum prüfen bestehender Dateien
PIL zum öffnen von Bildern
"""
import tkinter as tk
# from tkinter import ttk
import os
from PIL import Image, ImageTk

from database.db_init import create_database
from logic import empty_button

if os.path.exists("ALC.db"):
    pass                # geh weiter in der Datei
    print("Keine neue DB erstellt")  # debug
else:
    create_database()   # führe Funktion aus

root = tk.Tk()  # erstellt Objekt des Fensters, beginnt den mainloop

root.title("Auto Landlord CRM")  # Titel des Fensters
root.minsize(width=800, height=400)  # Mindestgoeße des Fensters in px
# root.maxsize()
root.geometry("1280x720")  # Standardgroeße des Fensters in px
root.resizable(width=True, height=True)  # Ob Groeße des Fensters bearbeitbar

banner = tk.Label(root,
                  text="ALC - Automated Landlord CRM",
                  font=("Arial", 25),
                  anchor="w")

banner.grid(row=0, column=0, columnspan=1, padx=0, pady=0)

check_house_icon = Image.open("graphics/house-30-512.png").resize((50, 50))
check_house_icon_tk = ImageTk.PhotoImage(check_house_icon)

gebaeude_add_button = tk.Button(root,
                                text=" Gebäude Verwalten ",
                                image=check_house_icon_tk,
                                compound="right",  # verbindet Text & Bild
                                font=("Arial", 25),
                                background="gray74",
                                command=empty_button)

gebaeude_add_button.grid(row=1, column=0, columnspan=1, padx=20, pady=20)

root.mainloop()  # Ereignissschleife innerhalb des Fensters
