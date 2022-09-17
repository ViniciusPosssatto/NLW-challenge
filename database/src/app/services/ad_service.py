from datetime import date
from src.app.models.ad import Ad


def create_ad(name, years_playing, discord, week_days, hour_start, hour_end, use_voice_channel, game_id, create_at = date.today()):
    # try:
        Ad.seed(
            name=name, 
            years_playing=years_playing, 
            discord=discord, 
            week_days=week_days, 
            hour_start=hour_start, 
            hour_end=hour_end,
            create_at=create_at, 
            use_voice_channel=use_voice_channel, 
            game_id=game_id
        )
        return ({"message": "Ad cadastrado com sucesso."})
    # except Exception:
    #     return Exception
    # except:
    #     return ({"error": "Erro ao cadastrar Ad."})