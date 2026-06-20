# This module is used to extract text from a PDF file
from pypdf import PdfReader

def extract_text_from_pdf(pdf_file):
    # Check if the user has uploaded a file
    if pdf_file is None:
        return ""
        
    try:
        # Create a PDF reader object
        reader = PdfReader(pdf_file)
        text = ""
        
        # Loop through all the pages in the PDF
        for page in reader.pages:
            # Extract text from the current page
            content = page.extract_text()
            # If content exists, add it to our main text variable
            if content:
                text = text + content + "\n"
                
        # Remove extra spaces from the beginning and end
        return text.strip()
        
    except Exception as e:
        # Return the error message if something goes wrong
        error_message = "Error reading PDF: " + str(e)
        return error_message