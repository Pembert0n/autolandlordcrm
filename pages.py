import tkinter as tk
from tkhtmlview import HTMLLabel
from main import root

def html_test_page():
    # Ausführen des HTML Codes
    with open("html_pages/test_page.html", "r", encoding="utf-8") as file:
        html_test = file.read()
    return HTMLLabel(root, html=html_test, padx=20, pady=20)
