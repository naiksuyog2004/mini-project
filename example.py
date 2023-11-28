import cv2
from pyzbar.pyzbar import decode
import time
from PIL import Image
import pdfplumber
import pandas as pd

cam = cv2.VideoCapture(0)
cam.set(5, 640)
cam.set(6, 480)

camera = True

while camera == True:
    success, frame = cam.read()

    cv2.imshow("QR Scanner", frame)

    if cv2.waitKey(1) == ord('s'):
        img_pil = Image.fromarray(frame)
        time_str = time.strftime('%Y-%m-%d-%H-%M-%S')
        img_pil.save(f'{time_str}.pdf')

        # Extract text from the generated PDF using pdfplumber
        with pdfplumber.open(f'{time_str}.pdf') as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()

        # Create a pandas DataFrame from the extracted text
        df = pd.read_csv(StringIO(text), delimiter='\t')

        # Save the DataFrame to a CSV file
        df.to_csv(f'{time_str}.csv', index=False)

        print(f"CSV file '{time_str}.csv' generated successfully!")