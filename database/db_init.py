"""sqlite 3 für Datenbank-Ebene."""
import sqlite3


def create_database():
    """Erstellt Datenbank mit benötigt Tabellen."""
    con = sqlite3.connect("ALC.db")
    cur = con.cursor()

    gebaeude = """
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

    wohnobjekt = """
        CREATE TABLE Wohnobjekt(
            ObjektID INT,
            WohnobjektID PRIMARY KEY,
            Groesse_in_m2 INT,
            letzte_renovierung DATE,
            anzahl_parkplatz INT,
            FOREIGN KEY (ObjektID) REFERENCES Gebaeude(ObjektID),
            FOREIGN KEY (ObjektID) REFERENCES Gebaeude(ObjektID)
        )
    """

    mieter = """
        CREATE TABLE Mieter(
            ObjektID INT,
            WohnobjektID INT,
            MieterID PRIMARY KEY,
            Vorname VARCHAR(255),
            Nachname VARCHAR(255),
            Geburtsdatum DATE,
            old_Postleitzahl INT(4),
            old_Strasse VARCHAR(255),
            old_Hausnr INT(5),
            old_Ortschaft VARCHAR(255),
            Kaltmiete FLOAT,
            Nebenkosten FLOAT,
            Muellkosten FLOAT,
            letzte_Mieterhöhung DATE
        )
    """

    cur.execute(gebaeude)
    cur.execute(wohnobjekt)
    cur.execute(mieter)
    print("create_database ausgeführt")  # debug
