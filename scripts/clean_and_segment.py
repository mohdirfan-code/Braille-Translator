import os
import re

PROCESSED_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')
CLEANED_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed', 'cleaned')
os.makedirs(CLEANED_DIR, exist_ok=True)

def clean_text(text):
    # Remove non-printable/control characters
    text = re.sub(r'[^\x09\x0A\x0D\x20-\x7E\u0900-\u097F]', '', text)
    # Replace multiple newlines with a single newline
    text = re.sub(r'\n{2,}', '\n', text)
    # Remove leading/trailing spaces on each line
    text = "\n".join([line.strip() for line in text.splitlines()])
    # Remove empty lines
    text = "\n".join([line for line in text.splitlines() if line.strip() != ""])
    return text

def segment_paragraphs(text):
    # Split on blank lines or double newlines for paragraphs
    paras = re.split(r'\n{2,}', text)
    # Further clean: remove empty, very short, or noise paragraphs
    paras = [p.strip() for p in paras if len(p.strip()) > 25]
    return paras

def process_file(filename):
    if not filename.endswith('.txt'):
        return
    inpath = os.path.join(PROCESSED_DIR, filename)
    outpath = os.path.join(CLEANED_DIR, filename.replace('.txt', '_cleaned.txt'))
    with open(inpath, 'r', encoding='utf-8') as f:
        raw = f.read()
    cleaned = clean_text(raw)
    paragraphs = segment_paragraphs(cleaned)
    # Save paragraphs, one per line
    with open(outpath, 'w', encoding='utf-8') as f:
        for para in paragraphs:
            f.write(para + '\n\n')
    print(f"Cleaned & segmented {filename} -> {os.path.basename(outpath)}")

def main():
    for fname in os.listdir(PROCESSED_DIR):
        process_file(fname)

if __name__ == '__main__':
    main()