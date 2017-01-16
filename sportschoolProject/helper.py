import string
import random
import qrController as qc
import cameraController as cc
import databaseController as dc
import time
import threading

def checkImage():
    starttime=time.time()
    while True:
        save_location = "C:/Users/User/Desktop/QRCodes/image.png"
        cc.takeImage(save_location)
        foundCode, code = qc.readQR(save_location)
        if(foundCode):
            if dc.compareCode(code):
                print("nice")
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