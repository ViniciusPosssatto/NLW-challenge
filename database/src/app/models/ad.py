from datetime import date
from src.app import database as db, ma
from src.app.models.game import Game


class Ad(db.Model):
    __tablename__ = 'ads'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    years_playing = db.Column(db.Integer, nullable=False)
    discord = db.Column(db.String(50), nullable=False)
    week_days = db.Column(db.String(50), nullable=False)
    hour_start = db.Column(db.Integer, nullable=False)
    hour_end = db.Column(db.Integer, nullable=False)
    use_voice_channel = db.Column(db.Boolean, nullable=False, default=False)
    create_at = db.Column(db.DateTime, nullable=False, default=date.today())
    game_id = db.Column(db.Integer, db.ForeignKey(Game.id), nullable = False)
    game = db.relationship("Game", foreign_keys=[game_id])

    def __init__(self, name, years_playing, discord, week_days, hour_start, hour_end, use_voice_channel, create_at, game_id):
        self.name = name
        self.years_playing = years_playing
        self.discord = discord
        self.week_days = week_days
        self.hour_start = hour_start
        self.hour_end = hour_end
        self.use_voice_channel = use_voice_channel
        self.create_at = create_at
        self.game_id = game_id
    
    @classmethod
    def seed(cls, name, years_playing, discord, week_days, hour_start, hour_end, use_voice_channel, create_at, game_id):
        ad = Ad(
        name = name,
        years_playing = years_playing,
        discord = discord,
        week_days = week_days,
        hour_start = hour_start,
        hour_end = hour_end,
        use_voice_channel = use_voice_channel,
        create_at = create_at,
        game_id = game_id
        )
        ad.save()

    def save(self):
        db.session.add(self)
        db.session.commit()


class AdSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'years_playing', 'discord', 'week_days', 'hour_start', 'hour_end', 'use_voice_channel', 'create_at', 'game_id')


ad_share_schema = AdSchema()
ads_share_schema = AdSchema(many=True)