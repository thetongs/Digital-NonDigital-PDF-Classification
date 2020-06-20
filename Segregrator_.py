import os
import PyPDF2

path = "Input/"

def digital_nondigital_checker(files):
    pdf_reader = PyPDF2.PdfFileReader(path + str(files), 'rb')
    total_pages = pdf_reader.getNumPages()
    curr_page = 0
    page_type_flag = False
    while total_pages:
        page_data = pdf_reader.getPage(curr_page)
        if '/Font' in page_data['/Resources']:          # Read resources of page
            print("The pdf page is digital.")
            total_pages -= 1
            curr_page += 1
            if(page_type_flag):
                print("The pdf is mixed.")
                break
        else:
            print("The pdf page is non digital.")
            total_pages -= 1
            curr_page += 1
            page_type_flag = True
    
    

if(__name__ == "__main__"):
    files = os.path.basename(path+'scansmpl.pdf')
    digital_nondigital_checker(files)