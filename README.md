# 🦾 Braille ETL Pipeline

## 📚 Project Overview

Welcome to the **Braille ETL Pipeline**!  
This project is an end-to-end, modular, and automated pipeline for converting raw text samples into **Grade 1 English Unicode Braille**, making content accessible for visually impaired users.  
It follows a classic **Extract, Transform, Load (ETL)** approach and is designed for clarity, reproducibility, and easy extension.

---

## 🗂️ Folder Structure

```
braille-etl-pipeline/
│
├── data/
│   ├── raw/              # Original data samples (input)
│   ├── processed/        # Cleaned and segmented text files
│   ├── output/           # Final Braille translations (output)
│   └── *.json            # Structured data as JSON (output from pipeline)
│
├── scripts/
│   ├── collect_samples.py      # For gathering or simulating input data
│   ├── extract_text.py         # Extracts text from raw files (e.g., PDFs, images)
│   ├── clean_and_segment.py    # Cleans and segments text into paragraphs/lines
│   ├── braille_translate.py    # Translates cleaned text to Grade 1 Braille (Unicode)
│   └── structure_to_json.py    # Converts structured output to JSON
│
├── requirements.txt   # Python dependencies for the project
└── README.md          # This documentation file
```

## 🚀 Key Features

- **Modular ETL Pipeline**: Each stage (collection, extraction, cleaning, translation, structuring) is a standalone script.
- **Batch Processing**: Handles multiple files/folders in one run.
- **Grade 1 English Braille**: Unicode mapping ensures output is both machine- and human-readable.
- **JSON Output**: For easy integration with other systems or analytics.
- **Clear Directory Separation**: Input, intermediate, and output data are kept organized for traceability.
- **Virtual Environment Support**: All dependencies isolated for reproducible results.
- **Demo Script Provided**: Easy guide for showcasing the pipeline in action.

---

## 🛠️ Setup & Usage

### 1. **Clone the Repository**
```sh
git clone https://github.com/mohdirfan-code/Braille-Translator.git
cd Braille-Translator-main
```

### 2. **Create and Activate a Virtual Environment**
```sh
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate
```

### 3. **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4. **Run the Pipeline Scripts**
- **Step 1:** Collect or place your raw data in `data/raw/`.
- **Step 2:** Extract text:
  ```sh
  python scripts/extract_text.py
  ```
- **Step 3:** Clean and segment text:
  ```sh
  python scripts/clean_and_segment.py
  ```
- **Step 4:** Translate to Braille:
  ```sh
  python scripts/braille_translate.py
  ```
- **Step 5:** Structure output as JSON:
  ```sh
  python scripts/structure_to_json.py
  ```

All outputs will appear in the `data/output/` or as a JSON file in `data/`.

---

## 💻 Workflow

1. Place your sample files (e.g., `.txt`, `.pdf`,`.jpg`) in `data/raw/`.
2. Run each script in order, or chain them as needed.
3. View the translated Braille output in `data/output/`.
4. Check the structured JSON output in `data/`.

---

## 🌟 Why Use This Pipeline?

- **Accessibility First:** Designed to make content accessible to all.
- **Reproducible Research:** Modular scripts and environments make it easy to retrace steps.
- **Open Source & Extendable:** Add more languages, input formats, or output types with minimal changes.
- **Educational Value:** Great for learning about ETL, accessibility, and text processing.

---

## 📊 Working Demo Video 

A demo video showing the pipeline in action ! 

[Watch the demo video here](https://drive.google.com/file/d/1LC9uHloRUpQWZuIDCH5PreOn5wgmi6-T/view?usp=sharing)

---

## 📝 Authors

- Mohd Irfan (@mohdirfan-code)

---

## 📝 Note 

- Make sure to activate your virtual environment before running scripts.
- If you add new scripts or data types, update this README for future users.
- For large files, consider using [Git LFS](https://git-lfs.github.com/).

---

**Happy Translating! 🦾⠓⠑⠇⠇⠕ ⠺⠕⠗⠇⠙!**
