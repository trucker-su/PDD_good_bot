filename = 'bileti_ab.pdf'

import minecart

pdffile = open(filename, 'rb')
doc = minecart.Document(pdffile)
page = doc.get_page(3)
for shape in page.shapes.iter_in_bbox((0, 0, 100, 200)):
	print (shape.path, shape.fill.color.as_rgb())
im = page.images[0].as_pil()  # requires pillow
im.show()