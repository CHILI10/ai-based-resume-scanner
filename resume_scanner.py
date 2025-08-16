import os
import re
import spacy
import pdfplumber
import docx
import json

# Load spaCy NLP model for Named Entity Recognition (NER)
nlp = spacy.load("en_core_web_sm")

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# Function to extract text from a DOCX file
def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Function to extract name, email, phone, and skills from text
def extract_details(text):
    details = {}
    
    # Extract email
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, text)
    details["Email"] = emails[0] if emails else "Not Found"
    
    # Extract phone number
    phone_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    phones = re.findall(phone_pattern, text)
    details["Phone"] = phones[0] if phones else "Not Found"
    
    # Extract name using NLP 
    doc = nlp(text)
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]

    if names:
        # Pick the longest name (usually full name, not "Gym")
        best_name = max(names, key=len)

        # Ignore names that look like project/website names
        ignore_words = ["project", "website", "resume", "cv"]
        if any(word.lower() in best_name.lower() for word in ignore_words):
            details["Name"] = "Not Found"
        else:
            details["Name"] = best_name
    else:
        details["Name"] = "Not Found"
    
    # Extract skills (basic keyword matching)
    skills = ["Python", "Java", "Machine Learning", "Data Science", "AI", "Deep Learning", "NLP", "SQL", "Excel"]
    found_skills = [skill for skill in skills if skill.lower() in text.lower()]
    details["Skills"] = found_skills if found_skills else "Not Found"

    return details

# Function to process resume and extract details
def process_resume(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif file_extension == ".docx":
        text = extract_text_from_docx(file_path)
    else:
        print("Unsupported file format!")
        return None

    details = extract_details(text)
    return details

# Main function
if __name__ == "__main__":
    import os
    import logging

# Suppress pdfminer font warnings
logging.getLogger("pdfminer").setLevel(logging.ERROR)
resume_path = input("Enter resume path or filename: ")
resume_path = resume_path if os.path.isabs(resume_path) else os.path.join(os.getcwd(), resume_path)

if not os.path.exists(resume_path):
    print("❌ File not found! Please provide a valid path or put the file in the same folder as this script.")
else:
    print("✅ Using resume file:", resume_path)
    # 👉 Continue with your resume processing here
    if os.path.exists(resume_path):
        extracted_details = process_resume(resume_path)
        if extracted_details:
            print(json.dumps(extracted_details, indent=4))
            with open("extracted_resume_details.json", "w") as f:
                json.dump(extracted_details, f, indent=4)
            print("Resume details saved as extracted_resume_details.json")
    else:
        print("File not found! Please provide a valid path.")
