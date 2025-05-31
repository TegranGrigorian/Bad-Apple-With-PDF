from fpdf import FPDF
from PIL import Image

class GeneratePdf():
	def __init__(self, pdf_path):
		self.pdf_path = pdf_path
		self.pixelmm = .264
	def generate(self, img_path):
		img = Image.open(img_path)
		imgw, imgh = img.size
		imgwmm = imgw * self.pixelmm
		imghmm = imgh * self.pixelmm
		pdf = FPDF()
		pdf.add_page()
		pagew = pdf.w
		pageh = pdf.h
		x = (pagew - imgwmm) // 2
		y = (pageh - imghmm) // 2
		pdf.image(img_path, x=x,y=y,w=imgwmm,h=imghmm)
		pdf.output(self.pdf_path)


