import re

SKILLS_DB = [
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
    normalized_text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        pattern = r"(?<![\w+#])" + re.escape(skill) + r"(?![\w+#])"
        if re.search(pattern, normalized_text):
            found_skills.append(skill)

    return sorted(found_skills)
