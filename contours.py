import cv2

img = cv2.imread('photos/abc.jpeg')

cv2.imshow('djd', img)

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(grey, (7,7), cv2.BORDER_DEFAULT)

canny = cv2.Canny(blur, 125, 175)
cv2.imshow('cascade', canny)

# using functions to find the contours
contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# cv2.RETR_ is a mode that determines what kind of contours is to be used, here LIST is used to find all the contours available
# CHAIN_APPROX_NONE is a method that approximates the values of the contours
print(f'{len(contours)} are the number of contours in the program')

cv2.waitKey(0)