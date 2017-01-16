import cv2

def takeImage(LOCATION):
    '''Maakt een foto en slaat deze op op de aangegeven locatie.
    LOCATION = Voorbeeld(C:/Users/User/Desktop/image.png)'''
    camera_port = 0
    ramp_frames = 30
    camera = cv2.VideoCapture(camera_port)
    
    def get_image():
        retval, im = camera.read()
        return im

    for i in range(0, ramp_frames):
        temp = get_image()
    print("Taking image...")
    camera_capture = get_image()
    cv2.imwrite(LOCATION, camera_capture)
    del(camera)