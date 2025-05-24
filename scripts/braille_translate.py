import os

CLEANED_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed', 'cleaned')
BRAILLE_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'output')
os.makedirs(BRAILLE_DIR, exist_ok=True)

# Grade 1 Braille Unicode Map
BRAILLE_MAP = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙',
    'e': '⠑', 'f': '⠋', 'g': '⠛', 'h': '⠓',
    'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇',
    'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏',
    'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
    'y': '⠽', 'z': '⠵',
    '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙',
    '5': '⠑', '6': '⠋', '7': '⠛', '8': '⠓',
    '9': '⠊', '0': '⠚',
    ' ': ' ',
    ',': '⠂', '.': '⠲', '?': '⠦', '!': '⠖',
    '-': '⠤', '\'': '⠄', ':': '⠒', ';': '⠆',
    '(': '⠶', ')': '⠶', '"': '⠶', '/': '⠌'
}

def detect_language(text):
    for c in text:
        if '\u0900' <= c <= '\u097F':
            return 'hi'
    return 'en'

def get_table(lang):
    return None  # Not needed anymore

def translate_to_braille(text, table):
    # Simple character-based Unicode Braille translator
    result = ''
    for char in text.lower():
        result += BRAILLE_MAP.get(char, '')  # skip unsupported
    return result

def process_file(filename):
    if not filename.endswith('_cleaned.txt'):
        return
    inpath = os.path.join(CLEANED_DIR, filename)
    outname = filename.replace('_cleaned.txt', '_braille.txt')
    outpath = os.path.join(BRAILLE_DIR, outname)
    with open(inpath, 'r', encoding='utf-8') as f:
        paras = [p.strip() for p in f.read().split('\n\n') if p.strip()]
    with open(outpath, 'w', encoding='utf-8') as f:
        for para in paras:
            lang = detect_language(para)
            if lang == 'hi':
                braille = "[Hindi not supported in this mode]"
            else:
                braille = translate_to_braille(para, None)
            f.write("TEXT: " + para + '\n')
            f.write("BRAILLE: " + braille + '\n\n')
    print(f"Braille translation done for {filename} -> {outname}")

def main():
    for fname in os.listdir(CLEANED_DIR):
        process_file(fname)

if __name__ == '__main__':
    main()
