import cv2
import numpy as np
from chapter6 import stackImages

img = cv2.imread('resources/shapes.png')
img_contour = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 1.)
canny = cv2.Canny(blur, 50, 50)

def find_contours(img):
	contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	for contour in contours:
		area = cv2.contourArea(contour)
		if area>500:
			cv2.drawContours(img_contour, contour, -1, (255, 0, 0), 3)
			perimeter = cv2.arcLength(contour, True)
			approx_corners = cv2.approxPolyDP(contour, 0.02*perimeter, True)
			n_corners = len(approx_corners)
			x, y, width, height = cv2.boundingRect(approx_corners)
			cv2.rectangle(img_contour, (x,y), (x+width,y+height), (0,255,0), 2)

			if n_corners==3: object_type = 'triangle'
			elif n_corners==4:
				if abs(1.-width/float(height))< .05:
					object_type = 'square'
				else:
					object_type = 'rectangle'
			elif n_corners>4: object_type = 'circle'
			else: object_type = 'unknown'

			cv2.putText(img_contour, object_type,
						(x+(width//2) -20, y+(height//2)),
						cv2.FONT_HERSHEY_COMPLEX, .5, (0,0,0), 2)


find_contours(canny)
black = np.zeros_like(img)
stacked = stackImages(.6, ([[img, gray, blur], [canny, img_contour, black]]))
cv2.imshow('Shapes', stacked)

cv2.waitKey(0)