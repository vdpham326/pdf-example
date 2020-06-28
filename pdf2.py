import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))

watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i) # get each page
    page.mergePage(watermark.getPage(0)) # merge page with the watermark page which only has 1 page; hence, the 0 index
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file: #create a watermarked_output file and write to that files all the info in output
        output.write(file)