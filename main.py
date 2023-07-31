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

add_house_icon = Image.open("graphics/house-add-512.png").resize((50, 50))
add_house_icon_tk = ImageTk.PhotoImage(add_house_icon)

label1 = tk.Label(root, text="Gebäude hinzufügen ",
                  image=add_house_icon_tk,
                  compound="right",
                  font=("Arial", 25))  # verbindet Text & Bild
label1.pack()

root.mainloop()  # Ereignissschleife innerhalb des Fensters
