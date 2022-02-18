# import cv2 as cv
# import ball_tracker.vision as vision
# from ball_tracker.enum.colors_enum import Colors
#
#
# if __name__ == '__main__':
#     # read image
#     img = cv.imread('assets/img1.jpg')
#
#     # isolate color
#     thresh = vision.filter_color(img, Colors.RED.value)
#
#     # find all contours in threshold image
#     # documentation:
#     # https://docs.opencv.org/4.5.5/d3/dc0/group__imgproc__shape.html#ga4303f45752694956374734a03c54d5ff
#     # https://docs.opencv.org/4.5.5/d3/dc0/group__imgproc__shape.html#ga819779b9857cc2f8601e6526a3a5bc71
#     contours, _ = cv.findContours(thresh, cv.CHAIN_APPROX_NONE, cv.RETR_EXTERNAL)
#
#     img_border = True
#     epsilon = 0.1
#     for contour in contours:
#         # skip first contour (image border)
#         if img_border:
#             img_border = False
#             continue
#
#         # approximate shape
#         approx = cv.approxPolyDP(contour,  epsilon * cv.arcLength(contour, True), True)
#
#         cv.drawContours(img, [contour], 0, (0, 255, 0), 5)
#
#         # find centroid
#         M = cv.moments(contour)
#         if M['m00'] != 0.0:
#             cx = int(M['m10'] / M['m00'])
#             cy = int(M['m01'] / M['m00'])
#
#         # if more than 8 edges, approximate to circle
#         if len(approx) > 8:
#             cv.putText(img, 'circle', (cx, cy), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
#
#         cv.imshow('shapes', img)
#
#         cv.waitKey(0)
#         cv.destroyAllWindows()

import cv2
import numpy as np
from matplotlib import pyplot as plt
import ball_tracker.vision as vision
from ball_tracker.enum.colors_enum import Colors

if __name__ == '__main__':
    # reading image
    img = cv2.imread('assets/img1.jpg')

    # converting image into grayscale image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # setting threshold of gray image
    threshold = vision.filter_color(img, Colors.RED.value)

    # using a findContours() function
    contours, _ = cv2.findContours(
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    i = 0

    # list for storing names of shapes
    for contour in contours:

        # here we are ignoring first counter because
        # findcontour function detects whole image as shape
        if i == 0:
            i = 1
            continue

        # cv2.approxPloyDP() function to approximate the shape
        approx = cv2.approxPolyDP(
            contour, 0.01 * cv2.arcLength(contour, True), True)

        # using drawContours() function
        cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)

        x, y = 0, 0

        # finding center point of shape
        M = cv2.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10'] / M['m00'])
            y = int(M['m01'] / M['m00'])

        # putting shape name at center of each shape
        if len(approx) == 3:
            cv2.putText(img, 'Triangle', (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        elif len(approx) == 4:
            cv2.putText(img, 'Quadrilateral', (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        elif len(approx) == 5:
            cv2.putText(img, 'Pentagon', (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        elif len(approx) == 6:
            cv2.putText(img, 'Hexagon', (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        else:
            cv2.putText(img, 'circle', (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # displaying the image after drawing contours
    cv2.imshow('shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
