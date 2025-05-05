import cv2
import numpy as np

image = cv2.imread('/Users/apple/Downloads/jackson-hendry-Gr68Qj2KI_0.jpg')

cv2.imshow('sdf', image)


def translate(img, x, y):  # translation - this function shifts the image in x and y axis
    translate_matrix = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, translate_matrix, dimensions)  # warpAffine function is responsible for transforming the image using the matrix

# -x --> to the left
# -y --> go up
# x --> to the right
# y --> go  down


translated = translate(image, 1000, -1739)
cv2.imshow('translated image', translated)

cv2.waitKey(0)
