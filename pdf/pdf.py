import PyPDF2

# with open("dummy.pdf", 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.getPage(0))  # getPage(1)

#  rotate counter-clockwise(90)
# with open("dummy.pdf", 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)


import sys

# inputs = sys.argv[1:]


# def pdf_combiner(pdf_list):
#     """
#     Combines separate pdfs into one file
#     """
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('super.pdf')


# pdf_combiner(inputs)

"""
Create watermarks on pdfs
"""


from PyPDF2 import PdfFileMerger, PdfFileReader

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open("watermarked_output.pdf", 'wb') as file:
        output.write(file)
