from datetime import date
from src.app.models.ad import Ad


def create_ad(name, hours_playing, discord, password, week_days, hour_start, hour_end, playing, game_id, create_at = date.today()):
    try:
        Ad.seed(
            name=name, 
            hours_playing=hours_playing, 
            discord=discord,
            password=password,
            week_days=week_days, 
            hour_start=hour_start, 
            hour_end=hour_end,
            create_at=create_at, 
            playing=playing, 
            game_id=game_id
        )
        return ({"message": "Ad cadastrado com sucesso."})
    except Exception:
        return Exception
    except:
        return ({"error": "Erro ao cadastrar Ad."})