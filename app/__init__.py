from flask import Flask, render_template, request, jsonify
import pdb
import sys
import os
import psycopg2
import random
import string
from dotenv import load_dotenv

from .database import db
from .werewolf_roles import roles
from .models import Game, Role_Assignment

app = Flask(__name__)
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
db.init_app(app)

app.app_context().push()
db.create_all()

@app.route('/')
def render_HTML():
    return render_template('index.html')

@app.route('/moderate')
def render_moderation_page():
    return render_template('moderate.html')

@app.route('/check')
def render_role_check():
    return render_template('checker.html')

@app.route('/distribute_role', methods=['POST'])
def distribute_role():
    inp = request.form.to_dict()
    type = inp['game_type']
    
    # Parse special wolves into input
    inp['special_wolf'] = request.form.getlist('special_wolf[]')
    del inp['game_type']
    if 'special_wolf[]' in inp:
        del inp['special_wolf[]']

    result = roles(inp)
    game_id = commit_roles_to_db(result, type)
    return jsonify({'roles': result, 'game_id': game_id})

@app.route('/check_role', methods=['GET'])
def check_role():
    inp = request.args.to_dict()
    result = Role_Assignment.query.filter_by(game_id=inp['game_id'],
                                             player_num=inp['player_num']).first()
    if result is None:
        return jsonify({'role': ''})
    else:
        return jsonify({'role': result.role})



def commit_roles_to_db(role_list, type_of_game):
    new_game_id = None

    # Select a non-repeated game ID.
    while True:
        candidate_id = generate_random_game_id()
        if Game.query.filter_by(id = candidate_id).first() is None:
            new_game_id = candidate_id
            break

    # Insert the game
    insert_game(new_game_id, type_of_game)

    # Insert the role
    for ix, role in enumerate(role_list):
        player_num = ix + 1
        assignment = Role_Assignment(new_game_id, player_num, role)
        print(assignment.__dict__)
        db.session.add(assignment)

    db.session.commit()
    return new_game_id

def insert_game(game_id, type_of_game):
    new_game = Game(game_id, type_of_game)
    print(new_game.__dict__)

    db.session.add(new_game)
    db.session.commit()

def generate_random_game_id(length = 6):
    all_chars = string.digits
    return ''.join([random.choice(all_chars) for i in range(length)])
