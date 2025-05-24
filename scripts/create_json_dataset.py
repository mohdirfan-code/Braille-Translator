import os
import json

BRAILLE_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'output')
JSON_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'json')
os.makedirs(JSON_DIR, exist_ok=True)

def process_braille_file(filename):
    inpath = os.path.join(BRAILLE_DIR, filename)
    result = {
        'source_file': filename,
        'paragraphs': []
    }
    with open(inpath, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')
        para = {}
        for line in lines:
            if line.startswith('TEXT: '):
                para['text'] = line.replace('TEXT: ', '')
            elif line.startswith('BRAILLE: '):
                para['braille'] = line.replace('BRAILLE: ', '')
            elif line.strip() == '':
                if para:
                    result['paragraphs'].append(para)
                    para = {}
        # Handle last para if file does not end with newline
        if para:
            result['paragraphs'].append(para)
    return result

def main():
    dataset = []
    for fname in os.listdir(BRAILLE_DIR):
        if fname.endswith('_braille.txt'):
            dataset.append(process_braille_file(fname))
    # Save one big JSON file
    json_path = os.path.join(JSON_DIR, 'braille_dataset.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)
    print(f"JSON dataset written to {json_path}")

if __name__ == '__main__':
    main()