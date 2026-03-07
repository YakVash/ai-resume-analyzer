from flask import Flask, render_template, request
import os
from resume_parser import extract_text
from skill_extractor import extract_skills
from matcher import match_resume

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    
    if request.method == "POST":
        file = request.files["resume"]
        job_desc = request.form["jobdesc"]

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        resume_text = extract_text(filepath)
        resume_skills = extract_skills(resume_text)

        match_score, missing_skills = match_resume(resume_skills, job_desc)

        result = {
            "skills": resume_skills,
            "score": match_score,
            "missing": missing_skills
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
