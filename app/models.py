from .database import db

class Role_Assignment(db.Model):
    __tablename__ = "role_assignment"
    game_id = db.Column(db.String(8), db.ForeignKey('game.id'),
                        primary_key = True)
    player_num = db.Column(db.Integer, primary_key = True)
    role = db.Column(db.String(20))

    def __init__(self, game_id, player_num, role):
        self.game_id = game_id
        self.player_num = player_num
        self.role = role

class Game(db.Model):
    __tablename__ = "game"
    id = db.Column(db.String(8), primary_key = True)
    type = db.Column(db.String(20))

    def __init__(self, id, type):
        self.id = id
        self.type = type

class Vote(db.Model):
    __tablename__ = "vote"
    game_id = db.Column(db.String(8), db.ForeignKey('game.id'),
                         primary_key = True)
    player_num = db.Column(db.Integer, primary_key = True)
    day = db.Column(db.Integer, primary_key = True)
    pk = db.Column(db.Integer, primary_key = True)
    vote_for = db.Column(db.Integer)

    def __init__(self, game_id, player_num, day, pk, vote_for):
        self.game_id = game_id
        self.player_num = player_num
        self.day = day
        self.pk = pk
        self.vote_for = vote_for
