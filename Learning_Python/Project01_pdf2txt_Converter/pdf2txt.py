# install pyPDF2 inside the virtual env using the below command
# pip3 install PyPDF2

import PyPDF2

# Open the PDF file in binary read mode
with open('sample.pdf', 'rb') as file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)
    
    # Get the number of pages in the PDF
    num_pages = len(pdf_reader.pages)
    
    # Create an empty string to store the text
    text = ''
    
    # Loop through each page and extract the text
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    
    # Open the output text file in write mode
    with open('sample.txt', 'w', encoding='utf-8') as output_file:
        # Write the extracted text to the file
        output_file.write(text)

print("PDF to text conversion complete!")