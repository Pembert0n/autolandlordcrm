import tkinter as tk    #Zeichnet Fenster
import os               #prüft vorhandene Datei

from database.db_init import create_database    #importiert Funktion aus anderer Datei

if os.path.exists("ALC.db"):
    pass                #geh weiter in der Datei
else:
    create_database()   #führe Funktion aus

root = tk.Tk()  #erstellt Objekt des Fensters, genannt root

root.title("Auto Landlord CRM") #Titel des Fensters
root.minsize(width=800, height=400) #Mindestgoeße des Fensters in px
#root.maxsize()
root.geometry("1280x720") #Standardgroeße des Fensters in px
root.resizable(width=True, height=True) #Einstellung ob die Groeße des Fensters bearbeitbar sein soll

label1 = tk.Label(root, text = "Auto Landlord CRM") #erstelle Label in Parent root
label1.pack()   #platziert label1 in root

root.mainloop() #Ereignissschleife innerhalb des Fensters
