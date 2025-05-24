import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
from bs4 import BeautifulSoup

RAW_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
PROCESSED_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')
os.makedirs(PROCESSED_DIR, exist_ok=True)

def extract_from_image(filepath):
    img = Image.open(filepath)
    text = pytesseract.image_to_string(img, lang="eng+hin")
    return text

def extract_from_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')
    # Try to extract main visible text only
    return soup.get_text(separator='\n', strip=True)

def extract_from_txt(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def process_file(filename):
    filepath = os.path.join(RAW_DIR, filename)
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        text = extract_from_image(filepath)
    elif filename.lower().endswith('.html'):
        text = extract_from_html(filepath)
    elif filename.lower().endswith('.txt'):
        text = extract_from_txt(filepath)
    else:
        print(f"Unsupported file type: {filename}")
        return
    # Save output as .txt file in processed/
    outname = os.path.splitext(filename)[0] + '.txt'
    outpath = os.path.join(PROCESSED_DIR, outname)
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Processed {filename} -> {outname}")

def main():
    for fname in os.listdir(RAW_DIR):
        process_file(fname)

if __name__ == '__main__':
    main()