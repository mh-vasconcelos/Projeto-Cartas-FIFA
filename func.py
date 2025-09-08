import json
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import math

# --- Função para carregar dados JSON ---
def load_artists(file_path="artists.json"):
    with open(file_path, "r") as f:
        return json.load(f)
    


# --- Função para gerar carta em PNG ---
def generate_card_mvp(artist):
    # Criar imagem em branco
    img = Image.new("RGB", (350, 400), color=(255, 215, 0))
    draw = ImageDraw.Draw(img)
    svg = 'preview (1).svg'
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



