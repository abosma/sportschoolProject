import qrcode
import os
from PIL import Image
#Om zbarlight werkend te krijgen op windows, gekopieerd van hun documentatie
zbar_path = os.path.join(os.environ['ProgramFiles'], 'zbar', 'bin')
os.environ['PATH'] = "{0};{1}".format(os.environ['PATH'], zbar_path)
import zbarlight

def createQR(DATA, LOCATION):
    '''Wordt gebruikt om een QR code te maken
    DATA = Data dat in de QR code gaat
    LOCATION = Opslagplek van de QR code met extensie
    Voorbeeld: C:/Users/User/Desktop/QRCodes/Foo.Bar.1A2B3C4D5E.png'''

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(DATA)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(LOCATION)

def readQR(LOCATION):
    '''Wordt gebruikt om een QR code te lezen
    LOCATION = Locatie van de image met extensie
    Voorbeeld: C:/Users/User/Desktop/QRCodes/Foo.Bar.1A2B3C4D5E.png'''

    try:
        with open(LOCATION, 'rb') as image_file:
            image = Image.open(image_file)
            image.load()

        codes = zbarlight.scan_codes('qrcode', image)
        code = str(codes[0],'utf-8')
        print("QR code: " + code)
        return (True, code)
    except:
        print("No QR code found")
        return (False, " ")