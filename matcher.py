def match_resume(resume_skills, job_desc):

    job_desc = job_desc.lower()

    job_skills = []

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

    for skill in skills_db:
        if skill in job_desc:
            job_skills.append(skill)

    matched = set(resume_skills).intersection(set(job_skills))
    missing = set(job_skills) - set(resume_skills)

    score = (len(matched) / len(job_skills)) * 100 if job_skills else 0

    return round(score,2), list(missing)