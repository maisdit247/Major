import cv2
import sys
from matplotlib import pyplot as plt
from ppadb.client import Client


# url de video
url = "http://192.168.1.24:4747/video"
# capture video de camera
capt = cv2.VideoCapture(url)
# detecteur de visage initier avec file
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

imagePath = r"moi7.png"
image = cv2.imread(imagePath)
while True:
    # read the image from the cam
    _, image = capt.read()
    # converting to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # detect all the faces in the image
    faces = face_cascade.detectMultiScale(image_gray, 1.3, 5)
    # for every face, draw a blue rectangle
    for x, y, width, height in faces:
        cv2.rectangle(
            image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2
        )
    cv2.imshow("image", image)
    if cv2.waitKey(1) == ord("q"):
        break

capt.release()
cv2.destroyAllWindows()
