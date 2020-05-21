from flask import Flask, render_template, request, jsonify
import pdb
import sys

app = Flask(__name__)

@app.route('/')
def render_HTML():
    return render_template('index.html')

@app.route('/distribute_role', methods=['GET'])
def distribute_role():
    input_form = request.form
    # TODO: Implement role distribution
    return jsonify(['Seer', 'Witch'])
