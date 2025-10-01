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
