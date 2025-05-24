# 🦾 Braille Translation Pipeline

## 📚 Assessment Overview

This project was developed as part of an assessment to create an automated pipeline that converts processed text into Grade 1 English Unicode Braille. The goal was to design a simple, robust, and efficient solution that can handle batches of text files, making them accessible for visually impaired users.

---

## 🔄 What We Did

- **Automated Pipeline:** Reads cleaned text files from a specified directory and outputs corresponding Braille translations.
- **Grade 1 English Braille:** Uses a Unicode mapping for Grade 1 English Braille, ensuring accurate and readable Braille output.
- **Batch Processing:** Handles multiple files in one run, writing outputs to a separate directory for easy access.
- **Language Detection:** Automatically checks for language, but only supports English for Braille output.
- **Clear Output:** Each output file contains both the original text and the Braille translation for reference.

---

## 🔧 How It Works

1. **Input:** Place your cleaned text files (ending with `_cleaned.txt`) in the `data/processed/cleaned/` directory.
2. **Processing:** Run the pipeline script. Each file is read, processed, and translated into Braille.
3. **Output:** The results are saved as new files in the `data/output/` directory, with `_braille.txt` appended to the name.

---

## 🚀 Usage

1. **Clone the repository:**
   ```sh
   git clone [Your GitHub Repo URL]
   cd [repo-folder]
   ```

2. **Set up your directories:**
   - Place input files in `data/processed/cleaned/`.
   - Ensure the `data/output/` directory exists (the script will create it if not).

3. **Run the script:**
   ```sh
   python pipeline_script.py
   ```

4. **Check your results:**
   - Translated files will appear in `data/output/`, with both the original text and the Braille translation.

---

## 💻 Example

Suppose you have a file `sample_cleaned.txt` containing:
```
Hello world!
```

The output in `data/output/sample_braille.txt` will be:
```
TEXT: Hello world!
BRAILLE: ⠓⠑⠇⠇⠕ ⠺⠕⠗⠇⠙⠖
```

---

## 🌟 Features

- Fast and easy-to-use
- Unicode Braille output (Grade 1 English)
- No external dependencies—fully portable Python solution
- Clear directory structure for reproducibility

---

## 🗃️ Directory Structure

```
repo/
├── data/
│   ├── processed/
│   │   └── cleaned/
│   └── output/
├── pipeline_script.py
└── README.md
```

---

## 🏁 Assessment Outcome

- The pipeline fulfills the requirements for batch Braille translation from processed text.
- The solution is easy to extend, maintain, and integrate into larger accessibility workflows.

---

## 📹 Demo Video

See the included demo video for a walkthrough of the pipeline’s functionality!

---

## 👨‍💻 Author

- [Your Name]