# AI Resume Analyzer

A Flask web application that parses a resume, extracts skills using NLP, and scores how well it matches a given job description — highlighting exactly which skills are missing.

## How It Works

1. User uploads a resume (PDF) and pastes a job description
2. `resume_parser.py` extracts raw text from the PDF using pdfminer
3. `skill_extractor.py` uses spaCy to identify technical skills from the resume text
4. `matcher.py` compares those skills against skills found in the job description and calculates a match score
5. The result is displayed — match percentage, matched skills, and missing skills

## Features

- PDF resume parsing
- NLP-based skill extraction using spaCy
- Job description skill matching with a scored percentage
- Missing skills highlighted so users know exactly what gaps exist
- Clean web interface built with Flask and HTML/CSS

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| NLP | spaCy, scikit-learn |
| PDF Parsing | pdfminer |
| Frontend | HTML, CSS |

## Project Structure

```
ai-resume-analyzer/
├── app.py               # Flask routes and app entry point
├── resume_parser.py     # Extracts text from uploaded PDF
├── skill_extractor.py   # NLP-based skill identification
├── matcher.py           # Compares resume skills to job description
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates
└── uploads/             # Temporary storage for uploaded resumes
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/YakVash/ai-resume-analyzer.git
cd ai-resume-analyzer

# Install dependencies
pip install -r requirements.txt

# Download spaCy language model
python -m spacy download en_core_web_sm

# Run the app
python app.py
```

Then open `http://localhost:5000` in your browser.

### Usage

1. Upload your resume as a PDF
2. Paste the job description into the text box
3. Click Analyze
4. View your match score and the list of missing skills

## Screenshots

> _Add screenshots here_

## Future Improvements

- Expand the skills database beyond the current keyword list
- Add support for DOCX resume format
- Use TF-IDF or semantic similarity for more accurate matching
- Deploy to a live URL (Render / Railway)

## License

This project is open source and available under the [MIT License](LICENSE).

