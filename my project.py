import cv2 as cv
import numpy as np
import copy

frame_width = 640
frame_height = 480
camera = cv.VideoCapture(0)  # we input '0' for default camera connected to the device
camera.set(3, frame_width)
camera.set(4, frame_height)
colors = [[5, 107, 0, 19, 255, 255],  # for orange
             [133, 56, 0, 159, 156, 255],  # for purple
             [57, 76, 0, 100, 255, 255]]   # for green

color_value = [[3, 102, 255],
                    [255, 0, 255],
                    [0, 255, 0]]

color_point = []


def identify_color(image, colors, color_value):
   img_filter = cv.cvtColor(image, cv.COLOR_BGR2HSV)  # HSV is a saturation filter
   count = 0
   new_points = []  # list to store the co-ordinate when the computer detects a colour
   for color in colors:
       lower = np.array(color[0:3])
       upper = np.array(color[3:])
       mask = cv.inRange(img_filter, lower, upper)
       x, y = get_contours(mask)
       cv.circle(image_clone, (x,y), 7, color_value[count], cv.FILLED)
       if x != 0 and y != 0:
          new_points.append([x, y, count])
       count += 1
   return new_points


def get_contours(mask_image):
    contours, hierarchies = cv.findContours(mask_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    # RETR_external is the mode and chain approx is the method
    x, y, w, h = 0, 0, 0, 0
    for i in contours:
        area = cv.contourArea(i)
        if area > 250:
            # cv.drawContours(image_clone, i, -1, (255, 0, 0), 3)
            perimeter = cv.arcLength(i, True)
            approximate = cv.approxPolyDP(i, 0.02*perimeter, True)
            x, y, w, h = cv.boundingRect(approximate)
    return x+w//2, y


def draw_points(color_point, color_value):
    for point in color_point:
        cv.circle(image_clone, (point[0], point[1]), 5, color_value[point[2]], cv.FILLED)


while True:
    isTrue, image = camera.read()
    image_clone = copy.copy(image)  # stores all the information of the image in the variable
    new_points = identify_color(image, colors, color_value)
    if len(new_points) != 0:
        for point in new_points:
            color_point.append(point)
    if len(color_point) != 0:
        draw_points(color_point, color_value)
    cv.imshow('camera', image_clone)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
