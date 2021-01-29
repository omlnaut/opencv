import cv2

print("Package imported")

def load_img():
	img = cv2.imread('resources/lena.png')
	cv2.imshow("Output", img)
	cv2.waitKey(0)

def load_video():
	cap = cv2.VideoCapture('resources/sample_video.mp4')
	while True:
		success, img = cap.read()
		cv2.imshow('Video', img)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

def webcam():
	cap = cv2.VideoCapture(0)
	cap.set(3, 640)
	cap.set(4, 480)
	cap.set(10, 100) #brightness

	while True:
		success, img = cap.read()
		cv2.imshow('Cam', img)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
