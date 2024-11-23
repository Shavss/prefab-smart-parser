# PDFtoDLM: Multi-File PDF to JSON Extraction Tool

This project provides a complete solution to upload multiple PDF files, visualize the PDFs in the frontend, and automatically generate corresponding JSON schemas using a backend processing pipeline with OpenAI's API. The JSON schemas are displayed in the frontend with an option to edit and download them.

## **Features**
- Upload multiple PDF files via the web interface.
- Immediate visualization of each uploaded PDF.
- Asynchronous generation of structured JSON data from each PDF.
- Interactive JSON schema editor with live syntax highlighting.
- Options to save edited JSON and download it locally.

## **Tech Stack**
- **Frontend**: React.js
- **Backend**: Node.js with Express
- **PDF Parsing**: pdf-parse, pdf-lib
- **AI Integration**: OpenAI API

## **Table of Contents**
1. [Installation](#installation)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [Customization](#customization)
6. [Screenshots](#screenshots)
7. [License](#license)

---

## **Installation**

### **Prerequisites**
- **Node.js** (v14 or higher)
- **npm** or **yarn**
- OpenAI API Key (requires a valid API key from [OpenAI](https://platform.openai.com/))
  
### **Backend Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pdf-extractor.git
   cd pdf-extractor

