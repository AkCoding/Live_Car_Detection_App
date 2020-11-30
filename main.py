import cv2

# import time

# Load the Cascade Classifier
car_cascade = cv2.CascadeClassifier("haarcascade_car.xml")

# startt  web cam
cap = cv2.VideoCapture('Traffic.mp4')