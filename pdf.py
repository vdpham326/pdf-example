import PyPDF2
import sys

inputs = sys.argv[1:] #will grab all the arguments from the command line into a list call 'inputs'


def pdf_combiner(pdf_list):
    #create a merger object 
    merger = PyPDF2.PdfFileMerger()
    #loop through pdf_list
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf) # add all the pdf files within the pdf_list
    
    # create a new pdf called super.pdf which combines all the pdf files
    merger.write('super.pdf')


pdf_combiner(inputs)