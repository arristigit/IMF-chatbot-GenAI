import uvicorn
from fastapi import FastAPI
from fastapi import HTTPException

from core.document_retriever import DocumentRetriever
from core.model_handler import ModelHandler
from core.pdf_processor import PDFProcessor
from schemas import QueryModel
from decouple import config

app = FastAPI()

# Instantiate necessary keys
OPENAI_API_KEY=config("OPENAI_API_KEY")
PDF_URL=config("PDF_URL")

# Download and process the PDF
pdf_processor = PDFProcessor(PDF_URL)
extracted_text = pdf_processor.extract_text()

# Initialize DocumentRetriever & ModelHandler
document_retriever = DocumentRetriever(extracted_text)
model_handler = ModelHandler(model_name="gpt-3.5-turbo", api_key=OPENAI_API_KEY)
model_handler.load_model()

# Routes handling
@app.get("/")
def home():
    return {"message": "Hello, this is IMF Report Chatbot"}

@app.post("/retrieve")
def retrieve(query: QueryModel):
    try:
        results = document_retriever.retrieve(query.query)
        if not results:
            raise HTTPException(status_code=404, detail="No relevant documents found.")
        return {"documents": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/summarize")
def summarize(text: QueryModel):
    try:
        summary = model_handler.get_summary(text.query)
        if not summary:
            raise HTTPException(status_code=404, detail="Could not generate summary.")
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/retrieve_and_summarize")
def retrieve_and_summarize(query: QueryModel):
    try:
        relevant_docs = document_retriever.retrieve(query.query)
        if not relevant_docs:
            return {"message": "No relevant documents found."}
        
        summaries = [model_handler.get_summary(doc) for doc in relevant_docs]
        return {"summaries": summaries}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

