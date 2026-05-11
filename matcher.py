from skill_extractor import extract_skills


def match_resume(resume_skills, job_desc):
    job_skills = extract_skills(job_desc)

    matched = set(resume_skills).intersection(set(job_skills))
    missing = set(job_skills) - set(resume_skills)

    score = (len(matched) / len(job_skills)) * 100 if job_skills else 0

    return round(score, 2), sorted(missing)
