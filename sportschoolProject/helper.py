import string
import random
import qrController as qc
import cameraController as cc
import databaseController as dc
import motorController as mc
import time
import datetime
import threading

def checkImage():
    starttime=time.time()
    while True:
        save_location = "C:/Users/User/Desktop/QRCodes/image.png"
        cc.takeImage(save_location)
        foundCode, code = qc.readQR(save_location)
        if(foundCode):
            if dc.compareCode(code):
                mc.openDoor()
            else:
                print("not nice")
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))

def checkImageThread():
    t = threading.Thread(target=checkImage)
    t.start()

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    '''Functie om een combinatie van letters en nummers te krijgen.
    Gebruik: VARIABLE = id_generator(AANTAL CHARACTERS)'''
    return ''.join(random.choice(chars) for x in range(size))

def eindDatum():
    '''Geeft datum 30 dagen van wanneer deze functie gerund wordt'''
    start_date = time.strftime("%d/%m/%Y")
    date_1 = datetime.datetime.strptime(start_date, "%d/%m/%Y")
    end_date = date_1 + datetime.timedelta(days=30)
    end_date = end_date.strftime("%d/%m/%Y")
    return(end_date)