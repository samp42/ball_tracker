import cv2

from ball_tracker.enum.colors_enum import Colors
from ball_tracker.pipeline.pipeline import Pipeline

if __name__ == '__main__':
    redPipeline = Pipeline(Colors.RED)
    bluePipeline = Pipeline(Colors.BLUE)

    img = cv2.imread('assets/img3.jpg')

    contours = redPipeline.process(img)

    # for contour in contours: