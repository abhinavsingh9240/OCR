import base64
import os.path

import cv2
import pytesseract


# import os


def get_text(path: str,language):
    # print("is file" , os.path.dirname(path))
    img = cv2.imread(path)
    print(img.shape)
    text = pytesseract.image_to_string(img, lang=language)

    return text


def get_boxes(path: str,language):
    img = cv2.imread(path)

    boxes = pytesseract.image_to_boxes(img, lang=language)
    hImg, wImg, _ = img.shape

    for b in boxes.splitlines():
        # print(b)
        b = b.split(' ')
        # print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])

        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 2)

    ret, frame_buff = cv2.imencode('.jpg', img)  # could be png, update html as well
    frame_b64 = base64.b64encode(frame_buff)

    return frame_b64.decode()
