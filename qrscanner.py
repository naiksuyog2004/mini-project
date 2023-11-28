import cv2
from pyzbar.pyzbar import decode
import time
from PIL import Image
cam = cv2.VideoCapture(0)
cam.set(5, 640)
cam.set(6, 480)

camera = True

while camera == True:
    success, frame = cam.read()

    # for i in decode(frame):
    #     print(i.type)
    #     print(i.data.decode('utf-8'))
    #     time.sleep(6)
    # cv2.waitKey(3)

    cv2.imshow("QR Scanner", frame)
    
    if cv2.waitKey(1) == ord('s'):
        img_pil = Image.fromarray(frame)
        time_str = time.strftime('%Y-%m-%d-%H-%M-%S')
        img_pil.save(f'{time_str}.pdf')
        print(time_str)