from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import datetime
import os

app = Flask(__name__)
GUESTBOOK_FILE = "guestbook.json"
