import tkinter as tk    #Zeichnet Fenster

root = tk.Tk()  #erstellt Objekt des Fensters, genannt root

label1 = tk.Label(root, text = "Auto Landlord CRM") #erstelle Label in Parent root
label1.pack()   #platziert label1 in root

root.mainloop() #Ereignissschleife innerhalb des Fensters