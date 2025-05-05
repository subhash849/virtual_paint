import cv2

image = cv2.imread('/Users/apple/Downloads/jackson-hendry-Gr68Qj2KI_0.jpg')

cv2.imshow('sdf', image)

def rotate_img(img, angle, centrePoint=None):
    (height, width) = img.shape[:2]

    if centrePoint is None:
        centrePoint = (height//2, width//2)

    rotate_matrix = cv2.getRotationMatrix2D(centrePoint, angle, 1.0)
    dimensions = (height, width)

    return cv2.warpAffine(img, rotate_matrix, dimensions)  # warpAffine function is responsible for transforming the image using the matrix


rotatedImage = rotate_img(image, 53)
cv2.imshow('rotated', rotatedImage)

cv2.waitKey(0)
