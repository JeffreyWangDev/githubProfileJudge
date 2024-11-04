import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted
import os
from dotenv import load_dotenv 
import requests
from flask import Flask, jsonify, render_template, send_from_directory
load_dotenv()

genai.configure(api_key=os.getenv('API_KEY'))

def get_github_profile(user):
    repo = requests.get(f"https://api.github.com/users/{user}/repos")
    repos = repo.json()
    profile = requests.get(f"https://github.com/{user}")
    profile = profile.text
    if repo.status_code != 200:
        return None, None
    return repos, profile

def generate_content(user):
    repos, profile = get_github_profile(user)
    if repos is None:
        return "Sorry, I couldn't find that user."
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content("Act like a rude, snarky, know-it-all kind of person.This is a github profile, THE FIRST WORD of the responce should be positive neutral or negative then give a rating out of 5 stars and then ONLY make a MEAN, SMART, KNOW-IT-ALL AND snarky reply about it unless this is a REALLY good profile. DO NOT give ways to improve the profile. This is the website for the profile "+str(repos)+str(profile))
    except ResourceExhausted:
        print("ResourceExhausted")
        try:
            model = genai.GenerativeModel("gemini-1.5-flash-8b")
            response = model.generate_content("Act like a rude, snarky, know-it-all kind of person.This is a github profile, THE FIRST WORD of the responce should be positive neutral or negative then give a rating out of 5 stars and then ONLY make a MEAN, SMART, KNOW-IT-ALL AND snarky reply about it unless this is a REALLY good profile. DO NOT give ways to improve the profile. This is the website for the profile "+str(repos)+str(profile))
        except ResourceExhausted:
            try:
                model = genai.GenerativeModel("gemini-1.0-pro")
                response = model.generate_content("Act like a rude, snarky, know-it-all kind of person.This is a github profile, THE FIRST WORD of the responce should be positive neutral or negative then give a rating out of 5 stars and then ONLY make a MEAN, SMART, KNOW-IT-ALL AND snarky reply about it unless this is a REALLY good profile. DO NOT give ways to improve the profile. This is the website for the profile "+str(repos)+str(profile))
            except ResourceExhausted:
                response = "Sorry, I'm out of ideas."
                return response
    return response.text

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.get("/")
def read_root():
    return render_template("index.html")

@app.get("/generate/<user>")
def generate(user):
    try:
        response = generate_content(user)
        rating = response.split()[0]
        response = ' '.join(response.split()[1:]).replace("★", "★\n", 1)
        return jsonify({"sentiment":rating.lower(),"text": response})
    except:
        return jsonify({"error": "Sorry, I couldn't find that user."})

if __name__ == "__main__":
    app.run()