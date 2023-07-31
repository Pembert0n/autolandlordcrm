"""
tkinter zum erstellen des Fensters
os zum prüfen bestehender Dateien
PIL zum öffnen von Bildern
"""
import tkinter as tk
from PIL import Image, ImageTk
from logic import empty_button

def main_page(root):
    """Startseite der Anwendung"""
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

    return root  # Gib das Frame der Startseite zurück
