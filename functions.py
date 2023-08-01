"""Probleme beim importieren der Variabeln,
da sich diese in einem Loop befinden?"""
# import tkinter as tk
# from tkhtmlview import HTMLLabel
# from main import startseite, gebaeude_page, back_to_main_page
import os
# from tkhtmlview import HTMLLabel
from database.db_init import create_database


def gebaeude_page_click(startseite, gebaeude_page, wohnung_page, back_to_main_page):
    """Ausführen des HTML Codes"""
    with open("html_pages/test_page.html", "r", encoding="utf-8") as file:
        html_test = file.read()
    startseite.set_html(html_test)
    gebaeude_page.grid_forget()
    wohnung_page.grid_forget()
    back_to_main_page.grid_forget()
    back_to_main_page.grid(row=0, column=0, padx=20, pady=20)


def haus_page_click(startseite, gebaeude_page, wohnung_page, back_to_main_page):
    """Ausführen des HTML Codes"""
    with open("html_pages/test_page_copy.html", "r", encoding="utf-8") as file:
        html_test = file.read()
    startseite.set_html(html_test)
    gebaeude_page.grid_forget()
    wohnung_page.grid_forget()
    back_to_main_page.grid_forget()
    back_to_main_page.grid(row=0, column=0, padx=20, pady=20)


def on_back_to_main_page_click(startseite, gebaeude_page, wohnung_page, back_to_main_page):
    """Ausführen des HTML Codes für die Startseite"""
    with open("html_pages/main_page.html", "r", encoding="utf-8") as file:
        html_startseite = file.read()
    startseite.set_html(html_startseite)
    back_to_main_page.grid_forget()
    gebaeude_page.grid(row=0, column=0, padx=20, pady=20)
    wohnung_page.grid(row=1, column=0, padx=20, pady=20)


def check_database():
    """Erstellt database nur wenn nicht vorhanden"""
    if os.path.exists("ALC.db"):
        print("Keine neue DB erstellt")  # debug
    else:
        create_database()
