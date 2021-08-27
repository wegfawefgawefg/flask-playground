import os
import json
import hashlib
from pprint import pprint

from flask import Flask, request
from flask import render_template, url_for
app = Flask(__name__)
KEY = "ea360b288b3dd178fe2625f55b2959bf1dba6eef"
DB = 'database.json'

# with open(DB, "w") as f:    
#     pprint(db)
#     db = json.dump(db, f)

@app.route("/login", methods=["GET", "POST"])
def login():
    exists = False
    display_greeting = False
    if request.method == 'POST':
        display_greeting = True
        username = request.form.get("username")
        password = request.form.get("password")
        print(f"{username}, {password}")
        if username and password:
            with open(DB, "r") as f:    
                db = json.load(f)
            m = hashlib.sha256()
            m.update(username.encode())
            m.update(password.encode())
            key = m.hexdigest()

            user_data = db["users"].get(username)
            if user_data:
                if key == user_data["key"]:
                    correct_userauth = True
                else:
                    correct_userauth = False
                    incorrect_userauth_reason = "Wrong Password..."
    return render_template("login.html", 
        display_greeting=display_greeting, 
        user=username,
        correct_userauth=correct_userauth,
        )

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        print(f"{username}, {password}")
        if username and password:
            with open(DB, "r") as f:    
                db = json.load(f)
            users = db["users"]
            if username in users:

            m = hashlib.sha256()
            m.update(username.encode())
            m.update(password.encode())
            key = m.hexdigest()

            user_data = db["users"].get(username)
            if user_data:
                if key == user_data["key"]:
                    correct_userauth = True
                else:
                    correct_userauth = False
                    incorrect_userauth_reason = "Wrong Password..."
    return render_template("login.html", 
        display_greeting=display_greeting, 
        user=username,
        correct_userauth=correct_userauth,
        )
@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    pass

@app.route("/", methods=["GET", "POST"])
def root():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)