"""
tkinter zum erstellen des Fensters
tkhtmlview zum anzeigen der html, hybrid software
os zum prüfen bestehender Dateien
PIL zum öffnen von Bildern
"""
import tkinter as tk
import os
from tkhtmlview import HTMLLabel
from database.db_init import create_database
from functions import on_next_page_click, on_back_to_main_page_click, check_database

if os.path.exists("ALC.db"):
    print("Keine neue DB erstellt")  # debug
else:
    create_database()

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

next_test_page = tk.Button(root, text="pls go 2", command=lambda: on_next_page_click(startseite, next_test_page, back_to_main_page))
next_test_page.grid(row=2, column=0, padx=20, pady=20)

back_to_main_page = tk.Button(root, text="Back to Main Page", command=lambda: on_back_to_main_page_click(startseite, next_test_page, back_to_main_page))

if __name__ == "__main__":
    check_database()
    root.mainloop()
