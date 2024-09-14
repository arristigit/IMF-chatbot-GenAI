import requests
import PyPDF2
from io import BytesIO

class PDFProcessor:
    def __init__(self, pdf_url: str):
        self.pdf_url = pdf_url
        self.text = None

    def download_pdf(self):
        response = requests.get(self.pdf_url)
        if response.status_code == 200:
            return BytesIO(response.content)
        else:
            raise Exception(f"Failed to download PDF. Status code: {response.status_code}")

    def extract_text(self):
        pdf_file = self.download_pdf()
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        
        self.text = text
        return text
