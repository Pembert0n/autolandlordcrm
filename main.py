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
# from pages import on_next_page_click, on_back_to_main_page_click


def on_next_page_click():
    """Ausführen des HTML Codes"""
    with open("html_pages/test_page.html", "r", encoding="utf-8") as file:
        html_test = file.read()
    startseite.set_html(html_test)
    next_test_page.grid_forget()  # Die Schaltfläche next_test_page ausblenden
    back_to_main_page.grid(row=2, column=0, padx=20, pady=20)
    # Die Schaltfläche back_to_main_page einblenden


def on_back_to_main_page_click():
    """Ausführen des HTML Codes für die Startseite"""
    with open("html_pages/main_page.html", "r", encoding="utf-8") as file:
        html_startseite = file.read()
    startseite.set_html(html_startseite)
    back_to_main_page.grid_forget()
    # Die Schaltfläche back_to_main_page ausblenden
    next_test_page.grid(row=2, column=0, padx=20, pady=20)
    # Die Schaltfläche next_test_page einblenden


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

next_test_page = tk.Button(root, text="pls go 2", command=on_next_page_click)
next_test_page.grid(row=2, column=0, padx=20, pady=20)

back_to_main_page = tk.Button(root, text="Back to Main Page",
                              command=on_back_to_main_page_click)

root.mainloop()
