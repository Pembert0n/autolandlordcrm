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

gebaeude_frame = tk.Frame(root)
# erstelle Container um Buttons darin nebeneinander zu plazieren

add_house_icon = Image.open("graphics/house-add-512.png").resize((50, 50))
add_house_icon_tk = ImageTk.PhotoImage(add_house_icon)

gebaeude_add_button = tk.Button(root,
                                text=" Gebäude hinzufügen ",
                                image=add_house_icon_tk,
                                compound="right",  # verbindet Text & Bild
                                font=("Arial", 25),
                                background="gray74",
                                command=empty_button)

gebaeude_add_button.grid(row=0, column=0, padx=20, pady=20)
# anchor -> Ausrichtung nach Himmelsrichtung
# pady/padx -> Seitenabstand

remove_house_icon = Image.open("graphics/house-remove-512.png").resize((50, 50))
remove_house_icon_tk = ImageTk.PhotoImage(remove_house_icon)

gebaeude_remove_button = tk.Button(root,
                                   text=" Gebäude entfernen ",
                                   image=remove_house_icon_tk,
                                   compound="right",  # verbindet Text & Bild
                                   font=("Arial", 25),
                                   background="gray74",
                                   command=empty_button)

gebaeude_remove_button.grid(row=0, column=1, padx=20, pady=20)

root.mainloop()  # Ereignissschleife innerhalb des Fensters
