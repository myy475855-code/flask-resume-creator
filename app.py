from flask import Flask, render_template, request, redirect, url_for, session
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for session storage

app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Home / Personal Info
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        
        
            
        session['personal_info'] = {
            'name': request.form.get('name'),
            'contact': request.form.get('contact'),
            'email': request.form.get('email'),
            'location': request.form.get('location'),
            'description': request.form.get('description'),
            'socials': []
        }
        
        photo_file = request.files.get('photo')
        photo_filename = None

        if photo_file and photo_file.filename != "":
            filename = secure_filename(photo_file.filename)
            photo_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            photo_file.save(photo_path)
            photo_filename = filename  
            session['personal_info'].append({'photo': photo_filename})
            
        for i in range(1, 6):
            site = request.form.get(f'social_site_{i}')
            link = request.form.get(f'social_link_{i}')
            if site and link:
                session['personal_info']['socials'].append({'site': site, 'link': link})

        return redirect(url_for('education'))
    return render_template("index.html")

# Education
@app.route("/education", methods=["GET", "POST"])
def education():
    if request.method == "POST":
        session['education'] = []
        entries = int(request.form.get('education_count', 0))
        for i in range(1, entries+1):
            school = request.form.get(f'school_{i}')
            degree = request.form.get(f'degree_{i}')
            gpa = request.form.get(f'gpa_{i}')
            start = request.form.get(f'start_{i}')
            end = request.form.get(f'end_{i}')
            notes = request.form.get(f'notes_{i}')
            if school and degree:
                session['education'].append({
                    'school': school, 'degree': degree, 'gpa': gpa,
                    'start': start, 'end': end, 'notes': notes
                })
        return redirect(url_for('experience'))
    return render_template("education.html")

# Experience
@app.route("/experience", methods=["GET", "POST"])
def experience():
    if request.method == "POST":
        session['experience'] = []
        entries = int(request.form.get('experience_count', 0))
        for i in range(1, entries+1):
            title = request.form.get(f'title_{i}')
            company = request.form.get(f'company_{i}')
            start = request.form.get(f'start_{i}')
            end = request.form.get(f'end_{i}')
            desc = request.form.get(f'description_{i}')
            if title and company:
                session['experience'].append({
                    'title': title, 'company': company,
                    'start': start, 'end': end, 'description': desc
                })
        return redirect(url_for('skills'))
    return render_template("experience.html")

# Skills
@app.route("/skills", methods=["GET", "POST"])
def skills():
    if request.method == "POST":
        session['skills'] = []
        entries = int(request.form.get('skills_count', 0))
        for i in range(1, entries+1):
            name = request.form.get(f'name_{i}')
            type_ = request.form.get(f'type_{i}')
            level = request.form.get(f'level_{i}')
            if name:
                session['skills'].append({'name': name, 'type': type_, 'level': level})
        return redirect(url_for('languages'))
    return render_template("skills.html")

# Languages
@app.route("/languages", methods=["GET", "POST"])
def languages():
    if request.method == "POST":
        session['languages'] = []
        entries = int(request.form.get('languages_count', 0))
        for i in range(1, entries+1):
            lang = request.form.get(f'language_{i}')
            level = request.form.get(f'level_{i}')
            if lang:
                session['languages'].append({'language': lang, 'level': level})
        return redirect(url_for('projects'))
    return render_template("languages.html")

# Projects
@app.route("/projects", methods=["GET", "POST"])
def projects():
    if request.method == "POST":
        session['projects'] = []
        entries = int(request.form.get('projects_count', 0))
        for i in range(1, entries+1):
            title = request.form.get(f'title_{i}')
            tech = request.form.get(f'tech_{i}')
            desc = request.form.get(f'description_{i}')
            github = request.form.get(f'github_{i}')
            live = request.form.get(f'live_{i}')
            if title:
                session['projects'].append({'title': title,'tech': tech,'description': desc,'github': github,'live': live})
        return redirect(url_for('certifications'))
    return render_template("projects.html")

# Certifications
@app.route("/certifications", methods=["GET", "POST"])
def certifications():
    if request.method == "POST":
        session['certifications'] = []
        entries = int(request.form.get('cert_count', 0))
        for i in range(1, entries+1):
            name = request.form.get(f'name_{i}')
            org = request.form.get(f'org_{i}')
            year = request.form.get(f'year_{i}')
            if name:
                session['certifications'].append({'name': name,'org': org,'year': year})
        return redirect(url_for('choose_template'))
    return render_template("certifications.html")

@app.route("/choose-template")
def choose_template():
    return render_template("templates.html")

@app.route("/preview1")
def preview1():
    return render_template("preview1.html", data=session)

@app.route("/preview2")
def preview2():
    return render_template("preview2.html", data=session)

@app.route("/preview3")
def preview3():
    return render_template("preview3.html", data=session)

@app.route("/preview4")
def preview4():
    return render_template("preview4.html", data=session)

@app.route("/preview5")
def preview5():
    return render_template("preview5.html", data=session)

@app.route("/preview6")
def preview6():
    return render_template("preview6.html", data=session)


if __name__ == "__main__":
    app.run(debug=True)
