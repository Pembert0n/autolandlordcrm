import sqlite3

#def create_database():
con = sqlite3.connect("ALC.db")
cur = con.cursor()

Gebaeude = """
    CREATE TABLE Gebaeude(
        ObjektID PRIMARY KEY,
        Postleitzahl INT(5),
        Ortschaft VARCHAR(255),
        Strasse VARCHAR(255),
        Hausnummer INT(4),
        Heizungsart VARCHAR(255),
        Anzahl Wohnobjekte INT(3)
    )
"""
cur.execute(Gebaeude)
con.commit
con.close
print("create_database ausgeführt") #debug
