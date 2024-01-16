# Arabic Document Classification Project

## Description
This project is designed to classify Arabic documents into seven distinct categories: Religion, Culture, Sports, Politics, Technology, Medical, and Finance. The process involves converting a given PDF document written in Arabic to an image, extracting text from this image, and then classifying the text using a BERT-based model. This is particularly useful in processing and categorizing Arabic documents without manual labeling.

## Installation

### Prerequisites
- Python 3.x
- Pip (Python package installer)

### Installation Steps
1. **Clone the Repository**:
   Clone this repository to your local machine using:

   ```bash
   git clone https://github.com/Jihed503/pdf-document-classification.git
   ```

2. **Install Required Python Packages**:
   Navigate to the project directory and install the required packages using pip:

   ```bash
   pip install Pillow pytesseract reportlab arabic-reshaper python-bidi fitz transformers torch
   ```

   Note: You may need to install additional system dependencies for `pytesseract`.

3. **Tesseract OCR**:
   Install Tesseract OCR, which is used for text extraction from images. Follow the instructions specific to your operating system from the [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract).

4. **Arabic Font**:
   Ensure you have an Arabic font installed, such as Arial. Update the `arabic_font_path` in the script to the location of your Arabic font file.

## Usage
To use the project, follow these steps:

1. **Prepare Your PDF Document**:
   Place the Arabic PDF document in the project directory. Ensure it's named 'arabic_doc.pdf' or update the `pdf` variable in the script accordingly.

2. **Run the Script**:
   Execute the Python script. It will convert the first page of the PDF to an image, extract the text, and then classify this text into one of the seven predefined categories.

3. **View the Results**:
   The script will print the extracted text and the predicted category to the console.

## Note
- The current script processes only the first page of the PDF. Modify the script if you need to process multiple pages.
- The accuracy of text extraction and classification depends on the quality of the PDF and the trained model.

## Contributing
Feel free to fork this project, make improvements, and open pull requests with your changes.
