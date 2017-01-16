import sqlite3

def createUser(NAAM, CODE, CANENTER=1):
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
    cursor = c.execute('SELECT EXISTS(SELECT * FROM USERS where NAAM=?)', (NAAM,))
    
    if cursor.fetchone()[0] == 0:
        c.execute("INSERT INTO USERS VALUES ("+
                  "NULL" + 
                  ",'" + NAAM + "'" + 
                  ",'" + CODE + "'" + 
                  ",'" + str(CANENTER) + 
                  "')")
        #c.execute("INSERT INTO USERDATA VALUES ("+
        #          "NULL" +
        #          ",NULL" +
        #          ",'" + 
        conn.commit()
        conn.close()
    else:
        print("USER " + NAAM + " is already in database sportschoolDatabase.db")
        return

def readUsers():
    '''Wordt gebruikt om alle users te weergeven uit de database.'''
    conn = sqlite3.connect("C:/Users/User/documents/visual studio 2015/Projects/sportschoolProject/sportschoolProject/sportschoolDatabase.db")
    c = conn.cursor()
    for row in c.execute('SELECT * FROM USERS'):
        print(row)
    conn.close()

def deleteUser(ID):
    '''Wordt gebruikt om een user te verwijderen uit de database.
    ID = ID van gebruiker die je wilt verwijderen'''
    conn = sqlite3.connect("C:/Users/User/documents/visual studio 2015/Projects/sportschoolProject/sportschoolProject/sportschoolDatabase.db")
    c = conn.cursor()
    try:
        c.execute("DELETE FROM USERS WHERE ID=?", (ID,))
        conn.commit()
    except Exception as e:
        print("No user found with ID: " + ID)
        print(e);
    conn.close()

def updateUser(ID, KEY, NEWVALUE):
    '''Wordt gebruikt om een user te updaten in de database.
    ID = ID van gebruiker die je wilt updaten
    KEY = De value die je wilt veranderen
    NEWVALUE = De nieuwe waarde van de value'''
    conn = sqlite3.connect("C:/Users/User/documents/visual studio 2015/Projects/sportschoolProject/sportschoolProject/sportschoolDatabase.db")
    c = conn.cursor()
    try:
        c.execute("UPDATE USERS SET " + KEY + "=? WHERE ID=?",(NEWVALUE, ID))
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
    cursor = c.execute('SELECT EXISTS(SELECT * FROM USERS where CODE=?)', (CODE,))
    
    if cursor.fetchone()[0] == 0:
        print("CODE " + CODE + " has not been found in the database")
        return False
    else:
        print("CODE " + CODE + " has been found in the database")
        data = c.execute("SELECT * FROM USERS where CODE=?", (CODE,))
        naam = data.fetchone()[1]
        naam = naam.replace(".", " ")
        print("Gebruiker: " + naam)
        return True