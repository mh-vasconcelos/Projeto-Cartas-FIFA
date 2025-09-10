# --- Arquivo que definir como atribuir as notas aos artistas e (opcional) chamar o RPA de imagem ---
import json
from datetime import datetime as dt
from func import load_artists
from rpa import search_img

# --- Gerador de overall, especificando os pesos para cada role ---
def ovr_singer(line):
    ovr = (line['COM'] * 0.3) + (line['TEC'] * 0.25) + (line['CAR'] * 0.2) + (line['ENA'] * 0.1) + (line['ARR'] * 0.1) + (line['CON'] * 0.05)
    return int(round(ovr, 0))

def ovr_guitar(line):
    ovr = (line['TEC'] * 0.3) + (line['ARR'] * 0.25) + (line['CAR'] * 0.15) + (line['COM'] * 0.15) + (line['ENA'] * 0.1) + (line['CON'] * 0.05)
    return int(round(ovr, 0))

def ovr_drum(line):
    ovr = (line['TEC'] * 0.35) + (line['ENA'] * 0.2) + (line['ARR'] * 0.2) + (line['CAR'] * 0.1) + (line['CON'] * 0.1) + (line['COM'] * 0.05)
    return int(round(ovr, 0))

def ovr_bass(line):
    ovr = (line['ARR'] * 0.3) + (line['TEC'] * 0.25) + (line['CON'] * 0.15) + (line['COM'] * 0.15) + (line['ENA'] * 0.1) + (line['CAR'] * 0.05)
    return int(round(ovr, 0))

# --- função que normaliza as funções (letras minusculas e com strip) ---
def _role_key(role):
    """Normaliza a role para comparação (tolerante a variações)."""
    if not role:
        return ""
    r = role.strip().lower()
    if r.startswith("guita"): 
        return "guitarist"
    if r.startswith("drum"):
        return "drummer"
    if r.startswith("bass"):
        return "bassist"
    if r.startswith("sing"):
        return "singer"
    return r

# --- Função que calcula o overall com base no role/função
def _calc_ovr_for(artist):
    role = _role_key(artist.get("role", ""))
    if role == "drummer":
        return ovr_drum(artist)
    if role == "singer":
        return ovr_singer(artist)
    if role == "bassist":
        return ovr_bass(artist)
    if role == "guitarist":
        return ovr_guitar(artist)
    
    # fallback: média simples
    vals = [artist.get(k, 0) for k in ("COM","TEC","CAR","ENA","ARR","CON")]
    return int(round(sum(vals)/len(vals))) if vals else 0

# --- Função que vai buscar a imagem do artista chamando search_img
def _get_img_for(artist):
    if not artist.get("img") or artist.get("img") == 0:
        try:
            return search_img(artist['nome'])
        except Exception as e:
            print(f"Erro ao buscar imagem para {artist.get('nome')}: {e}")
            return artist.get("img", 0)
    return artist.get("img")

# --- Função que vai centralizar toda a lógica das funções anteriores ---
def ovr_img(json_file, img=True, artists_file='artists.json'):
    # carrega novos (pode vir lista ou lista de listas)
    novos = load_artists(file_path=json_file) or []

    # achata caso load_artists retorne [[...]]
    if novos and isinstance(novos[0], list):
        flat = []
        for sub in novos:
            if isinstance(sub, list):
                flat.extend(sub)
            else:
                flat.append(sub)
        novos = flat

    # calcula OVR e busca imagem
    for artist in novos:
        if not isinstance(artist, dict):
            continue
        artist['role'] = artist.get('role', '').strip()
        artist['OVR'] = int(_calc_ovr_for(artist))
        artist['timestamp'] = dt.now().strftime("%d/%m/%y %H:%M:%S")
        if img:
            artist['img'] = _get_img_for(artist)

    # carrega já existentes, criando se necessário
    try:
        with open(artists_file, 'r', encoding='utf-8') as f:
            artists = json.load(f)
            if not isinstance(artists, list):
                artists = []
    except FileNotFoundError:
        artists = []

    # cria mapa (nome+role normalizados) -> índice em artists
    index_map = {}
    for i, a in enumerate(artists):
        key = (a.get('nome','').strip().lower(), _role_key(a.get('role','')))
        index_map[key] = i

    added = 0
    updated = 0

    for new_artist in novos:
        if not isinstance(new_artist, dict):
            continue
        key = (new_artist.get('nome','').strip().lower(), _role_key(new_artist.get('role','')))
        if key in index_map:
            # atualiza o registro existente (sobrescreve campos do existente)
            idx = index_map[key]
            # opcional: mesclar em vez de sobrescrever totalmente
            artists[idx].update(new_artist)
            updated += 1
        else:
            artists.append(new_artist)
            index_map[key] = len(artists) - 1
            added += 1

    # salva de volta
    with open(artists_file, 'w', encoding='utf-8') as f:
        json.dump(artists, f, indent=4, ensure_ascii=False)

    # limpa o JSON original (apaga conteúdo)
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump([], f, indent=4, ensure_ascii=False)

    print(f"Adicionados: {added} | Atualizados: {updated} | Total final em {artists_file}: {len(artists)}")
    return artists if novos else []

if __name__ == "__main__":
    ovr_img("artists_to_add.json", img=True)
