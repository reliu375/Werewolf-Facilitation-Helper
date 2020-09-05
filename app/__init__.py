from flask import Flask, render_template, request, jsonify
import pdb
import sys
import os
import psycopg2
import random
import string
from dotenv import load_dotenv
from sqlalchemy.exc import IntegrityError

from .database import db
from .werewolf_roles import roles, dual_roles
from .models import Game, Role_Assignment, Vote

app = Flask(__name__)
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
db.init_app(app)

app.app_context().push()
db.create_all()

# pdb.set_trace()
@app.route('/')
def render_HTML():
    return render_template('index.html')

@app.route('/moderate')
def render_moderation_page():
    return render_template('moderate.html')

@app.route('/check')
def render_role_check():
    return render_template('checker.html')

@app.route('/vote')
def render_vote():
    return render_template('vote.html')

@app.route('/assign')
def render_assign():
    return render_template('assign.html')

@app.route('/cast_vote', methods=['POST'])
def cast_vote():
    inp = request.form.to_dict()
    game_id = inp['game_id']
    player_num = inp['player_num']
    day = inp['day']
    pk = inp['pk']
    vote_for = inp['vote_for']

    vote = Vote(game_id, player_num, day, pk, vote_for)
    print(vote.__dict__)

    try:
        success_code = 1
        current_vote = Vote.query.filter_by(game_id = game_id,
                                            day = day,
                                            pk = pk,
                                            player_num = player_num).first()
        if current_vote is not None:
            db.session.delete(current_vote)
            db.session.commit()
            success_code = 2

        db.session.add(vote)
        db.session.commit()

        return jsonify({'success': success_code})
    except Exception as e:
        return jsonify({'success': 0})

@app.route('/get_vote', methods=['GET'])
def get_vote():
    inp = request.args.to_dict()
    result = Vote.query.filter_by(game_id = inp['game_id'],
                                  day = inp['day'],
                                  pk = inp['pk']).all()

    vote_dict = parse_vote_result(result)

    return jsonify({'success': 1, 'votes': vote_dict})

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

@app.route('/distribute_dual_role', methods=['POST'])
def distribute_dual_role():
    inp = request.form.to_dict()
    num_players = int(inp['num_players'])

    result = dual_roles(num_players)
    game_id = commit_roles_to_db(result, 'dual_werewolf')
    return jsonify({'roles': result, 'game_id': game_id})

@app.route('/check_role', methods=['GET'])
def check_role():
    inp = request.args.to_dict()
    game = Game.query.filter_by(id = inp['game_id']).first()
    if game is None:
        return jsonify({'role': ''})

    game_type = game.type

    player_num = int(inp['player_num'])

    if game_type == 'werewolf':
        result = Role_Assignment.query.filter_by(game_id=inp['game_id'],
                                                 player_num=inp['player_num']).first()
        if result is None:
            return jsonify({'role': ''})
        else:
            return jsonify({'role': result.role})
    elif game_type == 'dual_werewolf':
        player_ids = [player_num*2-1, player_num*2]
        roles = []
        for id in player_ids:
            result = Role_Assignment.query.filter_by(game_id=inp['game_id'],
                                                   player_num=id).first()
            roles.append(result.role)
            if result is None:
                return jsonify({'role': ''})

        return jsonify({'role': roles})
    else:
        return jsonify({'role': ''})


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

def parse_vote_result(result):
    vote_dict = {}
    for elt in result:
        if elt.vote_for not in vote_dict:
            vote_dict[elt.vote_for] = []
        vote_dict[elt.vote_for].append(elt.player_num)

    vote_dict = {key: ', '.join([str(num) for num in vote_dict[key]]) for key in vote_dict}

    return vote_dict
