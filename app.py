import os

from flask import Flask, flash, render_template, request
from werkzeug.utils import secure_filename

from resume_parser import extract_text
from skill_extractor import extract_skills
from matcher import match_resume

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf"}

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    
    if request.method == "POST":
        file = request.files.get("resume")
        job_desc = request.form.get("jobdesc", "").strip()

        if not file or file.filename == "":
            flash("Please upload a PDF resume.")
            return render_template("index.html", result=result)

        if not allowed_file(file.filename):
            flash("Only PDF resumes are supported right now.")
            return render_template("index.html", result=result)

        if not job_desc:
            flash("Please paste a job description before analyzing.")
            return render_template("index.html", result=result)

        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
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
