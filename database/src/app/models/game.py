from src.app import database as db, ma


class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    banner_url = db.Column(db.String(200), nullable=False)

    def __init__(self, title, banner_url):
        self.banner_url = banner_url
        self.title = title

    @classmethod
    def seed(cls, title, banner_url):
        game = Game(
        title = title,
        banner_url = banner_url,
        )
        game.save()

    def save(self):
        db.session.add(self)
        db.session.commit()

class GameSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'banner_url')


game_share_schema = GameSchema()
games_share_schema = GameSchema(many=True)
