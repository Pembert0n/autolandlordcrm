"""
tkinter zum erstellen des Fensters
tkhtmlview zum anzeigen der html, hybrid software
os zum prüfen bestehender Dateien
PIL zum öffnen von Bildern
"""
import tkinter as tk
# from tkinter import ttk
import os
from tkhtmlview import HTMLLabel
# from PIL import Image, ImageTk
from database.db_init import create_database
# from logic import empty_button


if os.path.exists("ALC.db"):
    # pass
    print("Keine neue DB erstellt")  # debug
else:
    create_database()   # führe Funktion aus

root = tk.Tk()  # erstellt Objekt des Fensters, beginnt den mainloop

root.title("Auto Landlord CRM")  # Titel des Fensters
root.iconbitmap("graphics/house-30-512.png")
root.minsize(width=800, height=400)  # Mindestgoeße des Fensters in px
# root.maxsize()
root.geometry("1280x720")  # Standardgroeße des Fensters in px
root.resizable(width=True, height=True)  # Ob Groeße des Fensters bearbeitbar

# Ausführen des HTML Codes
with open("html_pages/main_page.html", "r", encoding="utf-8") as file:
    html_startseite = file.read()

startseite = HTMLLabel(root, html=html_startseite)
startseite.grid(row=1, column=0, columnspan=1, padx=20, pady=20)

root.mainloop()  # Ereignissschleife innerhalb des Fensters
