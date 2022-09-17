from datetime import date, datetime, timedelta
from src.app.models.ad import Ad, ad_share_schema
from src.app.utils import generate_jwt


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


def make_login(discord, password):

    try:
        try:
            ad_query = Ad.query.filter_by(discord = discord).first_or_404()
        except:
            return {"error": "Dados inválidos"}
        
        ad = ad_share_schema.dump(ad_query)

        if not ad_query.check_password(password):
            return {"error": "Dados inválidos"}

        payload = {
            "name": ad['name'],
            "ad_id": ad_query.id,
            "expire": datetime.utcnow() + timedelta(days=1)
        }

        token = generate_jwt(payload)

        return {"token": token}
    except:
        return {"error": "Ops! Algo deu errado..."}
