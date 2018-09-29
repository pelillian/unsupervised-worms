import cv2

if __name__ == "__main__":
	mov = cv2.VideoCapture('mov/MVI_8510.MOV')
	success, img = mov.read()
	i = 0
	success = True
	while success and i < 5:
		cv2.imshow(img)
		success, img = mov.read()
		i += 1