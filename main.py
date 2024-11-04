import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted
from google.ai.generativelanguage_v1beta.types import content
import json
import typing_extensions as typing

class Responce (typing.TypedDict):
    response: str
    starRating: int
    rating: int
    
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_schema": list[Responce],
  "response_mime_type": "application/json",
}
import os
from dotenv import load_dotenv 
import requests
from flask import Flask, jsonify, render_template, send_from_directory
# load_dotenv()

genai.configure(api_key=os.getenv('API_KEY'))

def get_github_profile(user):
    repo = requests.get(f"https://api.github.com/users/{user}/repos")
    repos = repo.json()
    profile = requests.get(f"https://github.com/{user}")
    profile = profile.text
    if repo.status_code != 200:
        return None, None
    return repos, profile

def generate_content(user,style):
    style = style.lower()
    repos, profile = get_github_profile(user)
    if style == "mean":
        system_instruction ="Give it a rating out of 3, with 1 being the worst and a number of stars out of 5. Act like a rude, snarky, know-it-all kind of person.This is a github profile, MAKE SURE TO make a MEAN, SMART, KNOW-IT-ALL AND snarky reply about it unless this is a REALLY good profile. DO NOT give ways to improve the profile."
    else:
        system_instruction ="Give it a rating out of 3, with 1 being the worst and a number of stars out of 5. Act like a nice, helpful, and supportive person. This is a github profile, MAKE SURE TO make a NICE, SUPPORTIVE, AND HELPFUL reply about it unless this is a REALLY bad profile. DO NOT be mean or rude"
    if repos is None:
        print(response)
        return "Sorry, I couldn't find that user."
    try:
        model = genai.GenerativeModel("gemini-1.5-flash",generation_config=generation_config,system_instruction=system_instruction)
        response = model.generate_content(str(repos)+str(profile))
    except ResourceExhausted:
        print("ResourceExhausted")
        try:
            model = genai.GenerativeModel("gemini-1.5-flash-8b",generation_config=generation_config,system_instruction=system_instruction)
            response = model.generate_content(str(repos)+str(profile))
        except ResourceExhausted:
            try:
                model = genai.GenerativeModel("gemini-1.5-flash-002",generation_config=generation_config,system_instruction=system_instruction)
                response = model.generate_content(str(repos)+str(profile))
            except ResourceExhausted:
                
                response = "Sorry, I'm out of ideas."
                return response
    return response.text[:-2][1:]

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.get("/")
def read_root():
    return render_template("index.html")

@app.get("/generate/<user>/<style>")
def generate(user,style):
    response = generate_content(user,style)
    print(response)
    try:
        respjson = json.loads(response)
        response = "★"*int(respjson["starRating"])+"\n"+respjson["response"]
        sent = respjson["rating"]
    except:
        response = "Sorry, Error in generating response."
        sent = 0
    sentresp = ""
    if sent == 1:
        sentresp = "negative"
    elif sent == 2:
        sentresp = "neutral"
    elif sent == 3:
        sentresp = "positive"
    return jsonify({"sentiment":sentresp ,"text": response})


if __name__ == "__main__":
    app.run()