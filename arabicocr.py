from PIL import Image
import pytesseract
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from arabic_reshaper import reshape
from bidi.algorithm import get_display
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from ArabicOcr import arabicocr
import sys, fitz  

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='ara', config='--psm 1 --oem 3')
        return text
    except Exception as e:
        print(f"Error during text extraction: {e}")
        return "Error"



def create_pdf_with_text(text, output_pdf_path):
    try:
        arabic_font_path = 'arial.ttf'  # Replace with the path to your Arial (or other) Arabic font
        pdfmetrics.registerFont(TTFont("Arabic", arabic_font_path))

        pdf = canvas.Canvas(output_pdf_path, pagesize=letter)
        pdf.setFont("Arabic", 12)  # Set the font

        reshaped_text = get_display(reshape(text))
        paragraphs = reshaped_text.split('\n')

        y_position = 720
        line_height = 15

        for paragraph in paragraphs:
            pdf.drawString(72, y_position, paragraph)
            y_position -= line_height

        pdf.save()
    except Exception as e:
        print(f"Error during PDF creation: {e}")

# Convert pdf to image
pdf="arabic_doc.pdf"

doc = fitz.open(pdf)  # open document
pix = doc[0].get_pixmap()  # render page to an image
pix.save("document.png")  # store image as a PNG



# Example usage
image_path = r'document.png'
output_pdf_path = r'document.pdf'

text_from_image = extract_text_from_image(image_path)

# Print the extracted text for verification
print("Extracted Text:")
print(text_from_image)

# create_pdf_with_text(text_from_image, output_pdf_path)


from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "M47Labs/arabert_multiclass_news"  # replace with your model's name
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)


text = text_from_image
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)

import torch

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)

classes = ["religion", "culture", "sports", "politics", "tec", "medical", "finance"]
predicted_class_id = predictions.argmax().item()
print("Predicted class :", classes[predicted_class_id-1])

