import PyPDF2
import pytesseract
# from PIL import Image
from pdf2image import convert_from_path

# Ask user for file name
filename = input("Enter the name of the PDF file: ")

# Open the PDF file in read-binary mode
with open(filename, 'rb') as pdf_file:

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Get the total number of pages in the PDF document
    num_pages = len(pdf_reader.pages)

    page_text = ""

    # Loop through each page and extract the text
    for page in range(num_pages):

        # Get the page object
        pdf_page = pdf_reader.pages[page]

        # Convert the PDF page to a PIL Image object
        pil_image = convert_from_path(filename, first_page=page+1, last_page=page+1)[0]
        # pil_image = pdf_page.toImage()

        # Use pytesseract to extract text from the temporary image file
        image_text = pytesseract.image_to_string(pil_image)

        # Add the extracted text to the page text
        page_text += image_text

    # Save the extracted text to a file
    with open('output.txt', 'w') as output_file:
        output_file.write(page_text)




# import PyPDF2

# # ask user for file name
# filename = input("Enter the name of the PDF file: ")

# # Open the PDF file in read-binary mode
# with open(filename, 'rb') as pdf_file:
    
#     # Create a PDF reader object
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
    
#     # Get the total number of pages in the PDF document
#     num_pages = len(pdf_reader.pages)

#     page_text = ""
    
#     # Loop through each page and extract the text
#     for page in range(num_pages):
        
#         # Get the page object
#         pdf_page = pdf_reader.pages[page]
        
#         # Extract the text from the page
#         page_text += pdf_page.extract_text()
        
#     # Save the extracted text to a file
#     with open('output.txt', 'w') as output_file:
#         output_file.write(page_text)

