from datetime import date
from src.app import database as db, ma
from src.app.models.game import Game, game_share_schema


class Ad(db.Model):
    __tablename__ = 'ads'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    hours_playing = db.Column(db.Integer, nullable=False)
    discord = db.Column(db.String(50), nullable=False)
    week_days = db.Column(db.String(50), nullable=False)
    hour_start = db.Column(db.Integer, nullable=False)
    hour_end = db.Column(db.Integer, nullable=False)
    playing = db.Column(db.Boolean, nullable=False, default=False)
    create_at = db.Column(db.DateTime, nullable=False, default=date.today())
    game_id = db.Column(db.Integer, db.ForeignKey(Game.id), nullable = False)
    game = db.relationship("Game", foreign_keys=[game_id])

    def __init__(self, name, hours_playing, discord, week_days, hour_start, hour_end, playing, create_at, game_id):
        self.name = name
        self.hours_playing = hours_playing
        self.discord = discord
        self.week_days = week_days
        self.hour_start = hour_start
        self.hour_end = hour_end
        self.playing = playing
        self.create_at = create_at
        self.game_id = game_id
    
    @classmethod
    def seed(cls, name, hours_playing, discord, week_days, hour_start, hour_end, playing, create_at, game_id):
        ad = Ad(
        name = name,
        hours_playing = hours_playing,
        discord = discord,
        week_days = week_days,
        hour_start = hour_start,
        hour_end = hour_end,
        playing = playing,
        create_at = create_at,
        game_id = game_id
        )
        ad.save()

    def save(self):
        db.session.add(self)
        db.session.commit()


class AdSchema(ma.Schema):
    game = ma.Nested(game_share_schema)
    class Meta:
        fields = ('id', 'name', 'hours_playing', 'discord', 'week_days', 'hour_start', 'hour_end', 'playing', 'create_at', 'game_id', 'game')


ad_share_schema = AdSchema()
ads_share_schema = AdSchema(many=True)