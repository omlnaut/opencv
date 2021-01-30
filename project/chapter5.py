import cv2
import numpy as np

img = cv2.imread('resources/cards.jpg')

width,height = 250,350

#coordinates of corners in original image (warped)
pts1 = np.float32([[111,219], [287,188], [154,482], [352,440]])

# coordinates of corners in (hypothetical) unwarped image
pts2 = np.float32([[0,0], [width,0], [0, height], [width,height]])
mat = cv2.getPerspectiveTransform(pts1, pts2)

warped = cv2.warpPerspective(img, mat, (width,height))

cv2.imshow('Cards', img)
cv2.imshow('Warped', warped)
cv2.waitKey(0)