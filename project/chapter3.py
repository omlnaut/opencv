import cv2

img = cv2.imread('resources/lambo.png')
print(img.shape)

resized = cv2.resize(img, (300,200))
cropped = img[:200, 200:500]

cv2.imshow('Image', img)
cv2.imshow('Resized', resized)
cv2.imshow('Cropped', cropped)
cv2.waitKey(0)