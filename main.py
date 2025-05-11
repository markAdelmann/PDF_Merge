from PyPDF2 import PdfWriter
import os

pdf_list = []
# Choose a new name for the merged file below
my_filename = "my_merged_PDF"


def get_files():

    directory = "PDFs_to_merge"

    for filename in os.scandir(directory):
        if filename.is_file():
            print(os.path.relpath(filename))
            pdf_list.append(os.path.relpath(filename))

    pdf_list.sort()
    merge_pdfs(pdf_list)


def merge_pdfs(pdf_list):
    merger = PdfWriter()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(f"Merged_PDF/{my_filename}.pdf")
    merger.close()


get_files()
