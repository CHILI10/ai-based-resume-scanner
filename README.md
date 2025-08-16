# AI-Based Resume Scanner

An AI-powered Resume Scanner that extracts key details such as **Name, Email, Phone, and Skills** from resumes (PDF/DOCX) built with **PYTHON**, **NLP (spaCy)** and **PDF parsing (pdfplumber)**.

## Features

- Extracts Candidate Name, Email Adddress, Phone Number and Skills
- Supports PDF and DOCX formats
- Uses spaCy NLP for Named Entity Recognition (NER)
- Uses pdf plumber for PDF Parsing
- Saves extracted details in a structured JSON file


## Installation

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python resume_scanner.py
```

- Enter the file path or file name of the resume when prompted.
  * If the file is in the same folder in which script is present, just type the filename.
  * If it’s somewhere else, enter the full path.

- The extracted details will be displayed and saved in `extracted_resume_details.json`.

## Supported File Formats

- `.pdf` (Extracted using pdfplumber)
- `.docx` (Extracted using python-docx)



## Contributions / Credits  

- Original project by [Himanshu Dhiman] 
- Modified and maintained by [Siddhant Tyagi] **https://github.com/CHILI10**

My contributions include:

- Added dynamic file path handling (works for both filenames and full paths).

- Suppressed noisy PDF font warnings for a cleaner output.

- Improved name extraction logic using NLP to avoid false positives.

- Documented setup and usage clearly for beginner-friendly experience.

# License

This project is licensed under the MIT License.
See the LICENSE file for details.