"""
tkinter zum erstellen des Fensters
tkhtmlview zum anzeigen der html, hybrid software
os zum prüfen bestehender Dateien
PIL zum öffnen von Bildern
"""
import tkinter as tk
import os
# from tkinter import ttk
from PIL import Image, ImageTk
from tkhtmlview import HTMLLabel
from database.db_init import create_database
from functions import (gebaeude_page_click,
                       on_back_to_main_page_click,
                       haus_page_click,
                       check_database)


if os.path.exists("ALC.db"):
    # pass
    print("Keine neue DB erstellt")  # debug
else:
    create_database()

root = tk.Tk()  # erstellt Objekt des Fensters, beginnt den mainloop
"""Fenster Einstellungen"""
root.title("Auto Landlord CRM")  # Titel des Fensters
root.iconbitmap("graphics/house-30-512.png")
root.minsize(width=800, height=400)  # Mindestgoeße des Fensters in px
# root.maxsize()
root.geometry("1280x720")  # Standardgroeße des Fensters in px
root.resizable(width=True, height=True)  # Ob Groeße des Fensters bearbeitbar

"""Laden von Icons"""
check_house_icon = Image.open("graphics/house-30-512.png").resize((50, 50))
check_house_icon_tk = ImageTk.PhotoImage(check_house_icon)

# Ausführen des HTML Codes
with open("html_pages/main_page.html", "r", encoding="utf-8") as file:
    html_startseite = file.read()

startseite = HTMLLabel(root, html=html_startseite)
startseite.grid(row=0, column=1, columnspan=1, padx=20, pady=20)

gebaeude_page = tk.Button(root,
                          text=" Gebäude Verwalten ",
                          image=check_house_icon_tk,
                          compound="right",  # verbindet Text & Bild
                          font=("Arial", 25),
                          anchor="nw",
                          command=lambda:
                          gebaeude_page_click(startseite,
                                             gebaeude_page,
                                             wohnung_page,
                                             back_to_main_page))
gebaeude_page.grid(row=0, column=0, padx=20, pady=20)

wohnung_page = tk.Button(root,
                          text="Wohnungsverwaltung",
                          command=lambda:
                          haus_page_click(startseite,
                                             gebaeude_page,
                                             wohnung_page,
                                             back_to_main_page))

wohnung_page.grid(row=1, column=0, padx=20, pady=20)

back_to_main_page = tk.Button(root,
                              text="Zurück zur Startseite",
                              command=lambda:
                              on_back_to_main_page_click(startseite,
                                                         gebaeude_page,
                                                         wohnung_page,
                                                         back_to_main_page))

if __name__ == "__main__":
    check_database()
    root.mainloop()  # Ereignissschleife innerhalb des Fensters
