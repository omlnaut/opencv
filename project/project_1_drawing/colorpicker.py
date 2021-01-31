import cv2
import numpy as np

from util import *


cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640,240)

cv2.createTrackbar('Hue min', 'TrackBars', 0, 179, lambda x:x)
cv2.createTrackbar('Hue max', 'TrackBars', 179, 179, lambda x:x)
cv2.createTrackbar('Saturation min', 'TrackBars', 0, 255, lambda x:x)
cv2.createTrackbar('Saturation max', 'TrackBars', 255, 255, lambda x:x)
cv2.createTrackbar('Value min', 'TrackBars', 0, 255, lambda x:x)
cv2.createTrackbar('Value max', 'TrackBars', 255, 255, lambda x:x)

cap = setup_webcam()

while True:
	success, img = cap.read()

	img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	h_min = cv2.getTrackbarPos('Hue min', 'TrackBars')
	h_max = cv2.getTrackbarPos('Hue max', 'TrackBars')
	s_min = cv2.getTrackbarPos('Saturation min', 'TrackBars')
	s_max = cv2.getTrackbarPos('Saturation max', 'TrackBars')
	v_min = cv2.getTrackbarPos('Value min', 'TrackBars')
	v_max = cv2.getTrackbarPos('Value max', 'TrackBars')

	lower = np.array([h_min, s_min, v_min])
	upper = np.array([h_max, s_max, v_max])
	mask = cv2.inRange(img_hsv, lower, upper)

	img_result = cv2.bitwise_and(img,img, mask=mask)

	stacked = stackImages(.6, ([img, img_hsv, img_result]))

	cv2.imshow('result', stacked)
	cv2.waitKey(1)
