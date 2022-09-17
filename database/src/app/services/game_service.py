from src.app.models.game import Game


def create_game(title, banner_url):
    try:
        Game.seed(
            title=title,
            banner_url=banner_url
        )
        return ({"message": "Game cadastrado com sucesso."})
    except Exception:
        return Exception
    except:
        return {"error": "Erro ao cadastrar game."}