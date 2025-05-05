import cv2 as cv
import numpy as np

img = cv.imread('/Users/apple/Downloads/damian-markutt-T41noNW7esg.jpg')
print(img.shape)  # img.shape function tells us the height, breadth and colo channel

# creating a blank image to work with
blank = np.zeros((500, 500, 3), dtype='uint8')  # uint8 is a datatype for an image

blank[200:300, 300:400] = 0, 255, 0
cv.imshow('green image', blank)

# displaying a rectangle
cv.rectangle(blank, (34, 0), (250, 300), (255, 255, 0), thickness=4)  # we use cv.Filled to fill the inside of the shape or simply put the value -1
cv.imshow('rectangle', blank)

# displaying a circle
cv.circle(img, (250, 300), 500, (255, 0, 20),  thickness=-1)
cv.imshow('tree', img)

# displaying a line
cv.line(blank, (50, 50), (200, 200), (255, 0, 0), thickness=5)
cv.imshow('line', blank)

# write a text
cv.putText(img, 'whatsup!', (500,500), cv.FONT_HERSHEY_COMPLEX, 4.5, (0,0,255), 4 )
cv.imshow('text', img)

cv.waitKey(0)
