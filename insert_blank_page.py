# The code below adds a blank page after every page in the PDF file

#Before running the code 'pip install PyPDF2' module from this link https://pypi.org/project/PyPDF2/
from PyPDF2 import PdfReader, PdfWriter

dr = r"C:\Docs"
ldr = dr + r"\original.pdf"
writer = PdfWriter()

with open(ldr, "rb") as f:
	#supply file to reader
	reader = PdfReader(f)
	
	# get the total number for pages
	number_of_pages = len(reader.pages)
	
	for i in range(number_of_pages):
		page = reader.pages[i]
		writer.add_page(page)
		# add blank page after each page
		writer.add_blank_page(page)
  
		with open(dr + r"\new.pdf", "wb") as output_stream:
			writer.write(output_stream)
