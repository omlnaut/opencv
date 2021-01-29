import cv2
import numpy as np

img = cv2.imread('resources/lena.png')
kernel = np.ones((5,5), np.uint8)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
img_canny = cv2.Canny(img, 150, 200)
img_dilation = cv2.dilate(img_canny, kernel, iterations=1)
img_erode = cv2.erode(img_dilation, kernel, iterations=1)

cv2.imshow("Grayscale", img_gray)
cv2.imshow("Blurred", img_blur)
cv2.imshow("Canny", img_canny)
cv2.imshow("Dilated", img_dilation)
cv2.imshow("Eroded", img_erode)
cv2.waitKey(0)