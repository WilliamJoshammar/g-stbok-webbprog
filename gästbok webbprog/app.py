from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import datetime
import os

app = Flask(__name__)
GUESTBOOK_FILE = "guestbook.json"

def load_entries():
    if not os.path.exists(GUESTBOOK_FILE):
        return []
    with open(GUESTBOOK_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_entries(entries):
    with open(GUESTBOOK_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

@app.route("/")
def index():
    entries = load_entries()
    return render_template("base.html", entries=entries)

@app.route("/add", methods=["POST"])
def add_entry():
    entries = load_entries()
    entry = {
        "name": request.form.get("name", "Anonym"),
        "email": request.form.get("email", ""),
        "comment": request.form.get("comment", ""),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    entries.append(entry)
    save_entries(entries)
    return render_template("popup.html")

if __name__ == "__main__":
    app.run(debug=True)
