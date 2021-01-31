import cv2
import numpy as np

from util import *

#color = [0,211,29, 15,255,255]
#color = [135, 179, 158, 255, 0, 255]
color = [135, 158, 0,  179, 255, 255]

def find_color(img):
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	lower = np.array(color[:3])
	upper = np.array(color[3:])
	mask = cv2.inRange(hsv, lower, upper)

	#cv2.imshow('img', mask)
	return mask

cap = setup_webcam()
while True:
	success, img = cap.read()
	mask = find_color(img)
	stacked = stackImages(1., [[img, mask]])


	cv2.imshow('Cam', stacked)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()