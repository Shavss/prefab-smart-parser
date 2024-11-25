# PDFtoDLM: Multi-File PDF to JSON Extraction Tool

[AEC Hackathon Munich](https://www.tum-venture-labs.de/events/aec-hackathon-munich-edition/) : [MOD Smart Prefab challenge](https://github.com/mod-construction/prefab-smart-parser)

Testing both  [OpenAI](backend/openai) and [Claude](backend/claude) LLM APIs with a [frontend](frontend) than can load multiple PDF files, visualize the PDFs in the frontend, and automatically generate corresponding JSON schemas using a backend processing pipeline with OpenAI's API. The JSON schemas are displayed in the frontend with an option to edit and download them.

## **Features**
- Upload multiple PDF files via the web interface.
- Immediate visualization of each uploaded PDF.
- Asynchronous generation of structured JSON data from each PDF.
- Interactive JSON schema editor with live syntax highlighting.
- Options to save edited JSON and download it locally.

## **Tech Stack**

**OpenAI**

- **Frontend**: React.js
- **Backend**: Node.js with Express
- **PDF Parsing**: pdf-parse, pdf-lib
- **AI Integration**: OpenAI API

## **Installation**

### **Prerequisites**

**OpenAI backend**

- **Node.js** (v14 or higher)
- **npm** or **yarn**
- OpenAI API Key (requires a valid API key from [OpenAI](https://platform.openai.com/))

**Claude backend**

- **Python**
- Claude API Key
- [Installation](backend/claude/README.md)

## Commit history

* moved 'example output' to backend/openai/output
