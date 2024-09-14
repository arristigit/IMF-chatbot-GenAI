# GenAI-Powered Document Retrieval and Summarization Chatbot

This project is a FastAPI-based chatbot that helps users query and summarize information from the **IMF Annual Report 2022 Financial Statements**. The chatbot integrates a pre-trained Generative AI (GenAI) model to provide intelligent summaries of document sections based on user queries.

The project uses **OpenAI** for text summarization and **TF-IDF** based document retrieval to provide the most relevant text snippets from the report.

## Features

- Retrieve relevant sections from the IMF Annual Report 2022 based on user queries.
- Summarize long text sections using a Generative AI model (OpenAI GPT).
- Ensure the chatbot only responds to relevant questions related to the IMF report.
- If a question is unrelated, it responds with: _"Sorry, I don't have information related to your query."_.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (for serving the FastAPI app)
- OpenAI Python API
- PyPDF2 (for PDF extraction)
- Scikit-learn (for TF-IDF and cosine similarity)
- Pydantic

## Installation

1. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Clone the repository:**

    ```bash
    git clone https://github.com/arristigit/IMF-chatbot-GenAI
    cd IMF-chatbot-GenAI
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file:**

    In the root directory of your project, create a `.env` file and add your **OpenAI API key**.

    ```bash
    touch .env
    ```

    Add the following content to `.env`:

    ```bash
    OPENAI_API_KEY=your_openai_api_key_here
    PDF_URL="your_pdf_url"
    ```

## Usage

### 1. Extract Text from the PDF
The text of the **IMF Annual Report 2022** is extracted using `PyPDF2`. The document retrieval system is based on **TF-IDF** and **cosine similarity** to find relevant text snippets based on user queries.

### 2. Run the FastAPI Server
Once the dependencies are installed and the `.env` file is set up, you can start the FastAPI server.

```bash
uvicorn main:app --reload
```
The API will be available at http://127.0.0.1:8000.

### 3. API Endpoints
**POST** `/retrieve`
Retrieve relevant sections from the document based on a user query.

- **Request**:
    ```bash
    {
        "query": "What is the financial performance of IMF in 2022?"
    }
    ```
- **Response**:
    ```bash
    {
        "documents": [
            "The report details the financial performance of the IMF in 2022, including revenue and expenditure details."
        ]
    }
    ```

**POST** `/summarize`
Summarize the retrieved text using a Generative AI model (OpenAI GPT).

- **Request**:
    ```bash
    {
        "query": "The IMF focuses on global financial stability and supports member countries in achieving macroeconomic stability..."
    }
    ```
- **Response**:
    ```bash
    {
        "summary": [
            "The IMF promotes global financial stability and helps its member countries maintain economic balance."
        ]
    }
    ```

**POST** `/retrieve_and_summarize`
Retrieve relevant sections from the document and summarize the content.

- **Request**:
    ```bash
    {
        "query": "What are the IMF’s expenses in 2022?"
    }
    ```
- **Response**:
    ```bash
    {
        "summary": "The IMF’s expenses in 2022 include operational costs and other administrative expenses."
    }
    ```

## Project Structure
    .
    ├── main.py                      # FastAPI main application file
    ├── core                         # GenAI implementation files
    │   ├── document_retriever.py    # Handles document retrieval logic using TF-IDF
    │   ├── model_handler.py         # Manages the loading and configuration of GenAI models
    │   └── pdf_processor.py         # Download and process the PDF
    ├── output                       # Chatbot responses over user queries
    ├── schemas.py                   # Schema for API request body
    ├── requirements.txt             # Project dependencies
    ├── requirement_libs.txt         # List of main libraries (useful for setup on different OS)
    ├── .gitignore                   # Ignore unnecessary files
    └── README.md                    # Project README file

## Contributing
Feel free to contribute to this project by opening issues or submitting pull requests.
