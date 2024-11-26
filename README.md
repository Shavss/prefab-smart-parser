### Python Service  

**README.md**  

```markdown  
# Python Service: PDF Text and Table Extraction  

This repository contains a Python service that processes PDF files to extract text and tables, then converts the extracted content into structured data using OpenAI's models.  

## Features  
- Extracts text and tables from PDF files using `pdfplumber` or a similar library.  
- Utilizes OpenAI APIs for prompting and converting extracted content into structured data.  
- Receives PDF file paths from a web application and returns structured data in JSON format.  

## Technologies Used  
- Python 3.x  
- Libraries: `marker`, OpenAI API, `Flask`  

## Installation  

### Prerequisites  
- Python 3.11.10 or later  
- OpenAI API key  

### Steps  

1. **Clone the Repository**:  
   ```bash  
   git clone <repository-url>

2. secrets: Set OPENAI_API_KEY in secret.py file.

3. run python run.py
