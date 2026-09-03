'''
CV parser file

Turns CV PDFs into text to make it easer to read
'''

from pypdf import PdfReader
from docx import Document

def extract_text(path):
    filename = path.name if hasattr(path, "name") else path
    if filename.lower().endswith(".pdf"):
        reader = PdfReader(path)
        lst = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                lst.append(text)
        return "\n".join(lst)

    elif filename.lower().endswith(".docx"):
        doc = Document(path)
        lst = [p.text for p in doc.paragraphs]
        return "\n".join(lst)

    else:
        raise ValueError(f"Unsupported file type: {path}")

'''
Adding keywords
Note: This is just a sample and is not guaranteed to be on all CVs
'''
KEYWORDS = [
    "python", "r", "sql", "matlab", "excel",
    "machine learning", "data analysis", "statistics", "bioinformatics",
    "pcr", "western blot", "cell culture", "flow cytometry", "crispr",
    "microscopy", "chromatography", "mass spectrometry",
    "project management", "technical writing", "public speaking",
]

def match_keywords(text, keyword = KEYWORDS):
    text_lower = text.lower()
    found = []
    for kw in keyword:
        if kw in text_lower:
            found.append(kw)
    return found

print("")

'''
Quick verification tests
'''

if __name__ == "__main__":
    # print(extract_text("demo_cv.pdf")[:500])
    # print(len(extract_text("demo_cv.pdf")))
    print(repr(extract_text("demo_cv_scanned_no_text_layer.pdf")))
    print(len(extract_text('demo_cv.docx')))
    text = extract_text("demo_cv.pdf")
    hits = match_keywords(text)
    print(len(hits), hits)