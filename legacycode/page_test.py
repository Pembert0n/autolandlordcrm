"""Test Page Switch"""
import tkinter as tk


def page1(root):
    page = tk.Frame(root)
    page.grid()
    tk.Label(page, text='This is page 1').grid(row=0)
    tk.Button(page, text='To page 2', command=changepage).grid(row=1)


def page2(root):
    page = tk.Frame(root)
    page.grid()
    tk.Label(page, text='This is page 2').grid(row=0)
    tk.Button(page, text='To page 1', command=changepage).grid(row=1)


def changepage():
    global pagenum, root
    for widget in root.winfo_children():
        widget.destroy()
    if pagenum == 1:
        page2(root)
        pagenum = 2
    else:
        page1(root)
        pagenum = 1


pagenum = 1
root = tk.Tk()
page1(root)
root.mainloop()
