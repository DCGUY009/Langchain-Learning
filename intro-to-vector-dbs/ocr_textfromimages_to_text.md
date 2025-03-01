There are two methods in langchain to extract text from images within PDFs using **Tesseract OCR** and **RapidOCR**, then convert the extracted text into embeddings using **OpenAIEmbeddings** in LangChain.

---

## **Prerequisites:**
### **1. Tesseract OCR (Free & Open Source)**
- **Install Tesseract**:
  - **Windows**: Download and install from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki).
  - **Linux**: Install using:
    ```bash
    sudo apt install tesseract-ocr
    ```
  - **Mac**: Install via Homebrew:
    ```bash
    brew install tesseract
    ```
- **Python Dependencies**:
  ```bash
  pip install pytesseract pdf2image pillow langchain openai
  ```

---

### **2. RapidOCR (Free & Open Source)**
- **Install RapidOCR**:
  ```bash
  pip install rapidocr-onnxruntime pdf2image langchain openai
  ```

---

### **3. OpenAI API (Requires API Key, Paid)**
- Get an API key from [OpenAI](https://platform.openai.com/signup/).
- Costs depend on usage, but **text embeddings are charged per token**.
- Install OpenAI Python package:
  ```bash
  pip install openai
  ```
- Set your API key as an environment variable:
  ```bash
  export OPENAI_API_KEY="your-api-key-here"
  ```
  *(On Windows, use `set` instead of `export`.)*

---

## **Full Code: OCR + OpenAI Embeddings**
```python
import os
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
import openai
import cv2
import numpy as np
from rapidocr_onnxruntime import RapidOCR


# Set OpenAI API Key (Ensure it's set in env variables)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Path to Tesseract executable (Windows users)
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH  # Comment this on Linux/Mac


# Function to extract images from PDF
def extract_images_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    return images


# OCR using Tesseract
def extract_text_tesseract(images):
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img) + "\n"
    return text.strip()


# OCR using RapidOCR
def extract_text_rapidocr(images):
    ocr = RapidOCR()
    text = ""
    for img in images:
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)  # Convert PIL image to OpenCV format
        result, _ = ocr(img_cv)
        text += " ".join([r[1] for r in result]) + "\n"
    return text.strip()


# Function to get OpenAI embeddings
def get_embeddings(text):
    embeddings_model = OpenAIEmbeddings(model="text-embedding-ada-002")  # OpenAI's embedding model
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50)  # Split text into chunks
    texts = text_splitter.split_text(text)
    embeddings = embeddings_model.embed_documents(texts)
    return embeddings


if __name__ == "__main__":
    pdf_path = "sample.pdf"  # Change this to your PDF file

    # Step 1: Extract images from PDF
    images = extract_images_from_pdf(pdf_path)

    # Step 2: Choose OCR method (Uncomment one)
    extracted_text = extract_text_tesseract(images)  # Using Tesseract
    # extracted_text = extract_text_rapidocr(images)  # Using RapidOCR

    print("Extracted Text:\n", extracted_text)

    # Step 3: Get OpenAI Embeddings
    if extracted_text:
        embeddings = get_embeddings(extracted_text)
        print("Embeddings Generated! Shape:", len(embeddings), "chunks")
    else:
        print("No text extracted, check OCR settings.")
```

---

## **Explanation:**
1. **Extract Images from PDF**:  
   - Uses `pdf2image` to convert PDF pages into images.
2. **OCR Methods**:  
   - **Tesseract OCR** (pytesseract) - Free, but may require fine-tuning.  
   - **RapidOCR** (ONNX-based) - Faster, optimized for Chinese/English text.  
3. **Text Embeddings**:  
   - Uses `OpenAIEmbeddings` (`text-embedding-ada-002`) to convert text into vector embeddings.
4. **Text Splitting**:  
   - Uses LangChain’s `CharacterTextSplitter` to break text into manageable chunks for embeddings.

---

## **Costs & Considerations**
| **Component** | **Cost** |
|--------------|---------|
| **Tesseract OCR** | Free |
| **RapidOCR** | Free |
| **pdf2image (Image Extraction)** | Free |
| **OpenAI Embeddings** | Paid (depends on usage) |

- OpenAI’s **`text-embedding-ada-002`** costs **$0.0001 per 1,000 tokens**.
- 1,000 tokens ≈ 750 words.

---

## **Which OCR Should You Use?**
- **Tesseract OCR**: Best for general use, but may struggle with complex layouts.
- **RapidOCR**: Faster and better for structured documents, especially with tables.
