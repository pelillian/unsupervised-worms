import cv2

class VideoFrames:
	def __init__(self, background_file, video_file, bounding_box):
		self.bg = cv2.imread(background_file)
		self.bg = cv2.cvtColor(self.bg, cv2.COLOR_BGR2GRAY)
		self.mov = cv2.VideoCapture(video_file)
		self.framenum = 0

	def read(self):
		self.framenum += 1
		success, img = self.mov.read()
		if not success:
			return None
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		return img

if __name__ == "__main__":
	# bounding_box = (974, 422, 39, 52)
	bounding_box = (964, 417, 64, 64)
	frames = VideoFrames("bg.jpg", "mov/MVI_8510.MOV", bounding_box)

	img = frames.read()

	# save first frame so we can edit out worm and create background image
	# cv2.imwrite("img.jpg", img)

	# loop through images
	while img is not None and frames.framenum < 10:
		img = frames.read()
	print(i)