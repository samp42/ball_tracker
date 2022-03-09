import os.path
import datetime
import cv2

from ball_tracker.enum.colors_enum import Colors
from ball_tracker.pipeline.pipeline import Pipeline

if __name__ == '__main__':
    redPipeline = Pipeline(Colors.RED.value)
    # bluePipeline = Pipeline(Colors.BLUE)

    path = "./results/"

    filename = "img2"

    date = datetime.datetime.now()

    img = cv2.imread('assets/{}.jpg'.format(filename))

    contours = redPipeline.process(img)

    for contour in contours:
        print("found radius of {:.2f} centered at ({:.2f},{:.2f})".format(contour.radius, contour.x, contour.y))
        cv2.drawContours(img, contour.contour, -1, (0, 255, 0), 2)

        output_path = os.path.join(path, filename)

        if not os.path.exists(output_path):
            os.mkdir(output_path)

        cv2.imwrite('{}/{}_{}_contours.jpg'.format(output_path, filename, date), img)

    # for contour in contours:
