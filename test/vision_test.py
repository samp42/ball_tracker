import cv2 as cv


if __name__ == '__main__':
    imgColor = cv.imread('assets/img3.jpg', 1)
    cv.imshow("Image", imgColor)

    cv.waitKey(0)
    cv.destroyAllWindows()
