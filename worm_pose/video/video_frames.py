import cv2


class VideoFrames:
	def __init__(self, background_file, video_file):
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

	def release(self):
		self.mov.release()


if __name__ == "__main__":
	# bounding_box = (974, 422, 39, 52)
	bounding_box = (964, 417, 64, 64)
	frames = VideoFrames("bg.jpg", "mov/MVI_8510.MOV")

	img = frames.read()

	fgbg = cv2.createBackgroundSubtractorMOG2()

	# save first frame so we can edit out worm and create background image
	# cv2.imwrite("img.jpg", img)

	# loop through images to train mask
	while img is not None and frames.framenum < 300:
		img = frames.read()

		fgmask = fgbg.apply(img)
		cv2.imshow('frame',fgmask)

		# Press esc to exit
		if (cv2.waitKey(1) & 0xff) == 27: break

	frames = VideoFrames("bg.jpg", "mov/MVI_8510.MOV")

	img = frames.read()

	tracker = cv2.TrackerMedianFlow_create()
	track_success = tracker.init(img, bounding_box)

	# loop through images
	while img is not None:
		img = frames.read()

		# track_success, new_box = tracker.update(img)

		# # bounding box
		# if track_success:
		# 	top_left = (int(new_box[0]), int(new_box[1]))
		# 	bottom_right = (int(new_box[0] + new_box[2]), int(new_box[1] + new_box[3]))
		# 	cv2.rectangle(img, top_left, bottom_right, (255,0,0), 2, 1)
		# else :
		# 	break

		# cv2.imshow("Tracking", img)

		fgmask = fgbg.apply(img)
		cv2.imshow('frame',fgmask)

		# Press esc to exit
		if (cv2.waitKey(1) & 0xff) == 27: break

	frames.release()
