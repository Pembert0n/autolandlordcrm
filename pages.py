"""Probleme beim importieren der Variabeln,
da sich diese in einem Loop befinden?"""
# import tkinter as tk
# from tkhtmlview import HTMLLabel
from main import startseite, next_test_page, back_to_main_page


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
