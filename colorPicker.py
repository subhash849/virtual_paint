import cv2

path = '/Users/apple/Desktop/Screenshot 2021-09-10 at 12.20.11 AM.png'
img = cv2.imread(path)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('photo', img)
cv2.waitKey(0)
