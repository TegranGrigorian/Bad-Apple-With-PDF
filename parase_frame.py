import cv2
import os
#dont know if this works, I parsed with ffmpeg :)
class parse_frame():
	def __init__(self, video_path, dir):
		self.path = video_path
		self.dir = dir
	def extract_frame(self):
		capture = cv2.VideoCapture(self.path, cv2.CAP_FFMPEG)
		while True:
			ret, frame = capture.read()
			if not ret:
				break
			if ((num_frame // 60) == 1):
				filename = os.path.join(self.dir, f"{num_frame}-video_img")
				cv2.imwrite(filename, frame)
			num_frame += 1
		capture.release()
		print(f"extraced {num_frame - 1} frames")



#deez = parse_frame("moma", "deez")
#deez.extract_frame()
