# import cv2 as cv
#
# # Setup SimpleBlobDetector parameters.
# params = cv.SimpleBlobDetector_Params()
#
# # Change thresholds
# params.minThreshold = 10
# params.maxThreshold = 200
#
# # Filter by Area.
# params.filterByArea = True
# params.minArea = 1500
#
# # Filter by Circularity
# params.filterByCircularity = True
# params.minCircularity = 0.1
#
# # Filter by Convexity
# params.filterByConvexity = True
# params.minConvexity = 0.87
#
# # Filter by Inertia
# params.filterByInertia = True
# params.minInertiaRatio = 0.01
#
# # Create a detector with the parameters
# ver = (cv.__version__).split('.')
# if int(ver[0]) < 3:
#     detector = cv.SimpleBlobDetector(params)
# else:
#     detector = cv.SimpleBlobDetector_create(params)

# Standard imports
# import cv2 as cv
# import numpy as np
#
# if __name__ == '__main__':
#     # Read image
#     im = cv.imread("assets/IMG_1058.jpg", cv.IMREAD_GRAYSCALE)
#
#     # Set up the detector with default parameters.
#     detector = cv.SimpleBlobDetector()
#
#     # Detect blobs.
#     keypoints = detector.detect(im)
#
#     # Draw detected blobs as red circles.
#     # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
#     im_with_keypoints = cv.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255),
#                                          cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#
#     # Show keypoints
#     cv.imshow("Keypoints", im_with_keypoints)
#     cv.waitKey(0)

import cv2

if __name__ == '__main__':
	# read input image
	img = cv2.imread('assets/img1.jpg')

	# convert to grayscale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# threshold to binary
	thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)[1]

	# find contours
	# label_img = img.coresultspy()
	contour_img = img.copy()
	contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	contours = contours[0] if len(contours) == 2 else contours[1]
	index = 1
	isolated_count = 0
	cluster_count = 0
	for cntr in contours:
		area = cv2.contourArea(cntr)
		convex_hull = cv2.convexHull(cntr)
		convex_hull_area = cv2.contourArea(convex_hull)
		try:
			ratio = area / convex_hull_area
		except Exception:
			ratio = 1
		# print(index, area, convex_hull_area, ratio)
		# x,y,w,h = cv2.boundingRect(cntr)
		# cv2.putText(label_img, str(index), (x,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,255), 2)
		if ratio < 0.91:
			# cluster contours in red
			cv2.drawContours(contour_img, [cntr], 0, (0, 0, 255), 2)
			cluster_count = cluster_count + 1
		else:
			# isolated contours in green
			cv2.drawContours(contour_img, [cntr], 0, (0, 255, 0), 2)
			isolated_count = isolated_count + 1
		index = index + 1

	print('number_clusters:', cluster_count)
	print('number_isolated:', isolated_count)

	# save result
	cv2.imwrite("results/blobs_connected_result.jpg", contour_img)

	# show images
	cv2.imshow("thresh", thresh)
	# cv2.imshow("label_img", label_img)
	cv2.imshow("contour_img", contour_img)
	cv2.waitKey(0)
