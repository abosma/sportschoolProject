import sqlite3

def createUser(NAAM, GESLACHT, CODE, WOONPLAATS, POSTCODE, HUISNUMMER, EMAIL, GEBOORTEDATUM, LOCATIE, ABONNEMENT, EINDDATUM):
    '''Wordt gebruikt om een nieuwe user in de database te zetten.
    NAAM = Naam van gebruiker, voor en achternaam
    CODE = Een combinatie van voornaam, achternaam en een code
    dat een combinatie van letters en nummers is met de lengte van
    10 characters. De vnaam, anaam en code hebben punten tussen elkaar.
    Voorbeeld: Foo.Bar.1A2B3C4D5E
    CANENTER = Een optionele value, 0 betekent dat de gebruiker er niet in mag.
    Heeft een default value van 1.
    Zal een error geven als er een gebruiker met hetzelfde voornaam is
    '''
    conn = sqlite3.connect("C:/Users/User/documents/visual studio 2015/Projects/sportschoolProject/sportschoolProject/sportschoolDatabase.db")
    c = conn.cursor()
    locatieLijst = ["Amersfoort", "Amsterdam", "Utrecht", "Den Haag", "Lelystad"]
    abonnementenLijst = ["Kids", "Silver", "Gold", "Platinum"]
    cursor = c.execute('SELECT EXISTS(SELECT * FROM KLANT where naam=?)', (NAAM,))
    
    if cursor.fetchone()[0] == 0:
        if LOCATIE in locatieLijst:
            if ABONNEMENT in abonnementenLijst:
                c.execute("insert into KLANT values (?,?,?,?,?,?,?,?,?,?,?)", (None, NAAM, GESLACHT, CODE, WOONPLAATS, POSTCODE, HUISNUMMER, EMAIL, GEBOORTEDATUM, None, None))
                c.execute("SELECT klantID FROM KLANT WHERE naam = '" + NAAM + "'")
                klantID = c.fetchone()
                klantID = klantID[0]
                c.execute("insert into KLANT_APPARAAT values (?,?,?,?)", (klantID, "Crosstrainer", 0, 0))
                c.execute("insert into KLANT_APPARAAT values (?,?,?,?)", (klantID, "Hometrainer", 0, 0))
                c.execute("insert into KLANT_APPARAAT values (?,?,?,?)", (klantID, "Loopband", 0, 0))
                c.execute("insert into KLANT_APPARAAT values (?,?,?,?)", (klantID, "Roeitrainer", 0, 0))
                c.execute("insert into KLANT_APPARAAT values (?,?,?,?)", (klantID, "Krachtstation", 0, 0))
                c.execute("insert into KLANT_SPORTSCHOOL values (?,?,?)", (klantID, LOCATIE, 0))
                c.execute("insert into KLANT_ABONNEMENT values (?,?,?)", (klantID, ABONNEMENT, EINDDATUM))
                conn.commit()
                conn.close()
            else:
                conn.close()
                print("Abonnement value is onjuist, de opgegeven abonnement is: " + ABONNEMENT)
                return
        else:
            conn.close()
            print("Locatie value is onjuist, de opgegeven locatie is: " + LOCATIE)
            return
    else:
        print("USER " + NAAM + " is al in database sportschoolDatabase.db")
        return

def readUsers():
    '''Wordt gebruikt om alle users te weergeven uit de database.'''
    conn = sqlite3.connect("C:/Users/User/documents/visual studio 2015/Projects/sportschoolProject/sportschoolProject/sportschoolDatabase.db")
    c = conn.cursor()
    klantDict = {}
    for id, name in c.execute('SELECT klantID, naam FROM KLANT'):
        klantDict[id] = name
    conn.close()
    return klantDict


def readData(VAR, TABLE):
    conn = sqlite3.connect("C:/Users/User/documents/visual studio 2015/Projects/sportschoolProject/sportschoolProject/sportschoolDatabase.db")
    c = conn.cursor()
    dataList = []
    for x in c.execute('SELECT * FROM ' + TABLE + ' WHERE klantID = ' + VAR):
        dataList.append(x);
    conn.close()
    return(dataList)

def getTableNames(VAR, TABLE):
    conn = sqlite3.connect("C:/Users/User/documents/visual studio 2015/Projects/sportschoolProject/sportschoolProject/sportschoolDatabase.db")
    c = conn.cursor()
    cursor = c.execute('SELECT * FROM ' + TABLE + ' WHERE klantID = ' + VAR)
    columnNames = next(zip(*c.description))
    conn.close()
    return(columnNames)

def deleteUser(ID):
    '''Wordt gebruikt om een user te verwijderen uit de database.
    ID = ID van gebruiker die je wilt verwijderen'''
    conn = sqlite3.connect("C:/Users/User/documents/visual studio 2015/Projects/sportschoolProject/sportschoolProject/sportschoolDatabase.db")
    c = conn.cursor()
    try:
        c.execute("DELETE FROM KLANT_ABONNEMENT WHERE klantID=?", (ID,))
        c.execute("DELETE FROM KLANT_APPARAAT WHERE klantID=?", (ID,))
        c.execute("DELETE FROM KLANT_SPORTSCHOOL WHERE klantID=?", (ID,))
        c.execute("DELETE FROM KLANT WHERE klantID=?", (ID,))
        conn.commit()
    except Exception as e:
        print("No user found with ID: " + ID)
        print(e);
    conn.close()

def updateUser(TABLE, KEY, NEWVALUE, ID):
    '''Wordt gebruikt om een user te updaten in de database.
    ID = ID van gebruiker die je wilt updaten
    KEY = De value die je wilt veranderen
    NEWVALUE = De nieuwe waarde van de value'''
    conn = sqlite3.connect("C:/Users/User/documents/visual studio 2015/Projects/sportschoolProject/sportschoolProject/sportschoolDatabase.db")
    c = conn.cursor()
    try:
        c.execute("UPDATE " + TABLE + " SET " + KEY + "=? WHERE klantID=?",(NEWVALUE, ID))
        conn.commit()
    except Exception as e:
        print("No KEY found: " + KEY)
        print(e);
    conn.close()

def compareCode(CODE):
    '''Kijkt of de ingevoerde code in de Database zit
    CODE = String van code die gezocht wordt in de database.
    Return = True of False'''
    conn = sqlite3.connect("C:/Users/User/documents/visual studio 2015/Projects/sportschoolProject/sportschoolProject/sportschoolDatabase.db")
    c = conn.cursor()
    cursor = c.execute('SELECT EXISTS(SELECT * FROM KLANT where QRcode=?)', (CODE,))
    
    if cursor.fetchone()[0] == 0:
        print("QRcode " + CODE + " has not been found in the database")
        return False
    else:
        print("QRcode " + CODE + " has been found in the database")
        data = c.execute("SELECT naam FROM KLANT where QRcode=?", (CODE,))
        naam = data.fetchone()[0]
        naam = naam.replace(".", " ")
        print("Gebruiker: " + naam)
        return True

def getUserData(CODE):
    '''Geeft 5 lists met userdata terug
    CODE = String van code die gezocht wordt in de database.
    Return = 5 lists'''
    conn = sqlite3.connect("C:/Users/User/documents/visual studio 2015/Projects/sportschoolProject/sportschoolProject/sportschoolDatabase.db")
    c = conn.cursor()
    
    cursor = c.execute('SELECT type FROM KLANT, KLANT_APPARAAT WHERE KLANT.klantID = KLANT_APPARAAT.klantID AND KLANT.QRcode=?', (CODE,))
    apparaten = c.fetchall()
    apparatenLijst = []
    for x in apparaten:
        apparatenLijst.append(x[0])

    cursor = c.execute('SELECT verbrande_calorieen FROM KLANT, KLANT_APPARAAT WHERE KLANT.klantID = KLANT_APPARAAT.klantID AND KLANT.QRcode=?', (CODE,))
    calorieen = c.fetchall()
    calorieenLijst = []
    for y in calorieen:
        calorieenLijst.append(y[0])

    cursor = c.execute('SELECT aptijd FROM KLANT, KLANT_APPARAAT WHERE KLANT.klantID = KLANT_APPARAAT.klantID AND KLANT.QRcode=?', (CODE,))
    tijd = c.fetchall()
    tijdLijst = []
    for z in tijd:
        tijdLijst.append(z[0])

    zippedList = zip(apparatenLijst, calorieenLijst, tijdLijst)
    volleLijst = list(zippedList)
    temp = []
    eindLijst = []
    for x in volleLijst:
        temp = [x[1], x[2]]
        eindLijst.append(temp)
    return(eindLijst)

def getAdminData():
    conn = sqlite3.connect("C:/Users/User/documents/visual studio 2015/Projects/sportschoolProject/sportschoolProject/sportschoolDatabase.db")
    c = conn.cursor()

    cursor = c.execute('SELECT klantID FROM KLANT_SPORTSCHOOL')
    klanten = c.fetchall()
    klantenAantal = len(klanten)

    cursor = c.execute('SELECT klantID, locatie FROM KLANT_SPORTSCHOOL')
    locKlanten = c.fetchall()
    aantalAmsterdam = 0;
    aantalUtrecht = 0;
    aantalDenhaag = 0;
    aantalLelystad = 0;
    aantalAmersfoort = 0;
    for x in locKlanten:
        if x[1] == "Amsterdam":
            aantalAmsterdam += 1;
        elif x[1] == "Utrecht":
            aantalUtrecht += 1;
        elif x[1] == "Den Haag":
            aantalDenhaag += 1;
        elif x[1] == "Lelystad":
            aantalLelystad += 1;
        elif x[1] == "Amersfoort":
            aantalAmersfoort += 1
    return(klantenAantal, aantalAmsterdam, aantalUtrecht, aantalDenhaag, aantalLelystad, aantalLelystad)