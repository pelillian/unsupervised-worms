from video import VideoFrames

if __name__ == "__main__":

	frames = VideoFrames("bg.jpg", "mov/MVI_8510.MOV")

	img = frames.read()

	# loop through images
	while img is not None:
		fgmask = fgbg.apply(img)
		cv2.imshow('frame',fgmask)

		# Press esc to exit
		if (cv2.waitKey(1) & 0xff) == 27: break
		
		img = frames.read()

	frames.release()
