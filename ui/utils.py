import fitz  # PyMuPDF
import re

def extract_mcqs_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    # Regex to capture MCQ format
    pattern = r"(\d+)\.\s*(.*?)\nA\)\s*(.*?)\nB\)\s*(.*?)\nC\)\s*(.*?)\nD\)\s*(.*?)\nAnswer:\s*([A-D])"
    matches = re.findall(pattern, text, re.DOTALL)

    mcqs = []
    for match in matches:
        _, question, a, b, c, d, ans = match
        mcqs.append({
            "question": question.strip(),
            "option_a": a.strip(),
            "option_b": b.strip(),
            "option_c": c.strip(),
            "option_d": d.strip(),
            "correct_answer": ans.strip()
        })
    return mcqs
