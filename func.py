import json
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import math
from jinja2 import Template
from xml.sax.saxutils import escape
# import cairosvg
from card_code import SVG_TEMPLATE, SVG_INICIAL

# --- Função para carregar dados JSON ---
def load_artists(file_path="artists.json"):
    with open(file_path, "r") as f:
        return json.load(f)
    


# --- Função para gerar carta em PNG ---
def generate_card_mvp(artist):
    # Criar imagem em branco
    img = Image.new("RGB", (350, 400), color=(255, 215, 0))
    draw = ImageDraw.Draw(img)
    # Fonte (pode precisar ajustar caminho da fonte no seu sistema)
    try:
        font_title = ImageFont.truetype("arial.ttf", 24)
        font_text = ImageFont.truetype("arial.ttf", 18)
    except:
        font_title = font_text = None  # usa fonte padrão

    # Cabeçalho (nome + role)
    draw.text((10, 10), f"{artist['nome']} ({artist['role']})", fill="white", font=font_title)

    # Atributos
    y_offset = 100
    for attr in ["ENA", "COM", "ARR", "TEC", "CON", "CAR"]:
        draw.text((20, y_offset), f"{attr}: {artist[attr]}", fill="white", font=font_text)
        y_offset += 40
    draw.text((20, y_offset), f"OVR: {artist['OVR']}", fill='black', font=font_title)
    y_offset += 60

    return img


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



