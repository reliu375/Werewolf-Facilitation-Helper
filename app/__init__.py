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

@app.route('/distribute_role', methods=['POST'])
def distribute_role():
    inp = request.form.to_dict()
    type = inp['game_type']
    del inp['game_type']
    result = roles(inp)
    commit_roles_to_db(result, type)
    return jsonify(result)

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

def insert_game(game_id, type_of_game):
    new_game = Game(game_id, type_of_game)
    print(new_game.__dict__)

    db.session.add(new_game)
    db.session.commit()

def generate_random_game_id(length = 6):
    all_chars = string.digits
    return ''.join([random.choice(all_chars) for i in range(length)])
