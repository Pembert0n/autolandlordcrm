import tkinter as tk    #Zeichnet Fenster

root = tk.Tk()  #erstellt Objekt des Fensters, genannt root

root.title("Auto Landlord CRM") #Titel des Fensters
root.minsize(width=800, height=400) #Mindestgröße des Fensters in px
#root.maxsize()
root.geometry("1280x720") #Standardgröße des Fensters in px
root.resizable(width=True, height=True) #Einstellung ob die Größe des Fensters bearbeitbar sein soll

label1 = tk.Label(root, text = "Auto Landlord CRM") #erstelle Label in Parent root
label1.pack()   #platziert label1 in root

root.mainloop() #Ereignissschleife innerhalb des Fensters
