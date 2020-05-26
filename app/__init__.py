from flask import Flask, render_template, request, jsonify
import pdb
import sys
import os
import psycopg2
from dotenv import load_dotenv

from .werewolf_roles import roles

app = Flask(__name__)
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

@app.route('/')
def render_HTML():
    return render_template('index.html')

@app.route('/distribute_role', methods=['GET'])
def distribute_role():
    result = roles(request.args.to_dict())
    return jsonify(result)
