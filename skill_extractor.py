import spacy

nlp = spacy.load("en_core_web_sm")

skills_db = [
    "python",
    "java",
    "c++",
    "machine learning",
    "data analysis",
    "flask",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "nlp"
]

def extract_skills(text):

    doc = nlp(text.lower())
    found_skills = []

    for token in doc:
        if token.text in skills_db:
            found_skills.append(token.text)

    return list(set(found_skills))