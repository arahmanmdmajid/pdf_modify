from PyPDF2 import PdfReader, PdfWriter

dr = r"C:\Docs"
ldr = dr + r"\original.pdf"
writer = PdfWriter()

with open(ldr, "rb") as f:
	#suply file to reader
	reader = PdfReader(f)
	
	number_of_pages = len(reader.pages)
	
	for i in range(number_of_pages):
		page = reader.pages[i]
		writer.add_page(page)
		writer.add_blank_page(page)
  
		with open(dr + r"\new.pdf", "wb") as output_stream:
			writer.write(output_stream)
