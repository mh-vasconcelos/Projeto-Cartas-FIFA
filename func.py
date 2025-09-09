import json
# import cairosvg
from card_code import SVG_TEMPLATE, SVG_INICIAL
import random

# --- Função para carregar dados JSON ---
def load_artists(file_path="artists.json"):
    with open(file_path, "r") as f:
        return json.load(f)


# def svg_to_png(svg_str, output_path="card.png"):
#     cairosvg.svg2png(bytestring=svg_str.encode('utf-8'), write_to=output_path)

def generate_card_svg(artist):
    svg_filled = SVG_TEMPLATE.format(
        NAME=artist['nome'],
        ROLE=artist.get('role',''),
        COUNTRY=artist.get('country',''),
        ENA=artist['ENA'], COM=artist['COM'],
        ARR=artist['ARR'], TEC=artist['TEC'],
        CON=artist['CON'], CAR=artist['CAR'],
        OVR=artist['OVR'], img=artist['img']
    )
    SVG_TOTAL = SVG_INICIAL + svg_filled
    with open("SVG.txt", "w") as arquivo:
        arquivo.write(SVG_TOTAL)
    # svg_to_png(svg_filled, output_path=f"{artist['nome'].replace(' ','_')}.png")
    return SVG_TOTAL  # opcional: exibir / salvar SVG também


def pick_band(artists):
    """
    Seleciona uma banda com 1 vocal, 1 guitarra, 1 baixo e 1 bateria.
    """
    band = []
    roles = ["Singer", "Guitarrist", "Bassist", "Drummer"]
    pool = artists[:]  # cópia da lista pra não alterar a original
    
    for role in roles:
        # Filtra os candidatos da role
        candidates = [a for a in pool if a.get("role") == role]
        if candidates:
            pick = random.choice(candidates)
            band.append(pick)
            pool.remove(pick)
        
    return band
