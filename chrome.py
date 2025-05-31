#import pyautogui
import subprocess
#path = "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
class chrome():
	def __init__(self, pdf):
		self.pdf = pdf
	def open_chrome(self):
	        # Launch Chrome in a separate process without waiting
		self.process = subprocess.Popen([
			"/mnt/c/Program Files/Google/Chrome/Application/chrome.exe",
			self.pdf
		], shell=False)
		print("Chrome opened.")
		print("open")
	def close_chrome(self):
		subprocess.run(["/mnt/c/Windows/System32/taskkill.exe", "/F", "/IM", "chrome.exe"], check=True)
		print("Chrome closed.")

