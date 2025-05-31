import pyautogui
import webbrowser


class chrome():
	def __init__(self, pdf):
		self.pdf = pdf
	def open_chrome(self):
		webbrowser.open_new_tab(self.pdf);

	def close_chrome(self):
		pyautogui.hotkey("ctrl", "w")
  
	def reloadfaggot(self):
		pyautogui.hotkey("f5")


