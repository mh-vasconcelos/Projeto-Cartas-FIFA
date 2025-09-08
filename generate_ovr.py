import json
from datetime import datetime as dt
from func import load_artists
# Gerador de overall, especificando os pesos para cada role
def ovr_singer(line):
    ovr = (line['COM'] * 0.3) + (line['TEC'] * 0.25) + (line['CAR'] * 0.2) + (line['ENA'] * 0.1) + (line['ARR'] * 0.1) + (line['CON'] * 0.05)
    return int(round(ovr,0))

def ovr_guitar(line):    
    ovr = (line['TEC'] * 0.3) + (line['ARR'] * 0.25) + (line['CAR'] * 0.15) + (line['COM'] * 0.15) + (line['ENA'] * 0.1) + (line['CON'] * 0.05)
    return int(round(ovr,0))

def ovr_drum(line):
    ovr = (line['TEC'] * 0.35) + (line['ENA'] * 0.2) + (line['ARR'] * 0.2) + (line['CAR'] * 0.1) + (line['CON'] * 0.1) + (line['COM'] * 0.05)
    return int(round(ovr))

def ovr_bass(line):
    ovr = (line['ARR'] * 0.3) + (line['TEC'] * 0.25) + (line['CON'] * 0.15) + (line['COM'] * 0.15) + (line['ENA'] * 0.1) + (line['CAR'] * 0.05)
    return int(round(ovr,0))


# Gerador de overall geral (olha para todos os dados do json)
def ovr(json_file):
    novos = load_artists(file_path=json_file)

    
    # calcula ovr dos novos
    for artist in novos:
        if artist['role'] == 'Drummer':
            artist['OVR'] = ovr_drum(artist)
            artist['timestamp'] = dt.now().strftime("%d/%m/%y %H:%M:%S")
        elif artist['role'] == 'Singer':
            artist['OVR'] = ovr_singer(artist)
            artist['timestamp'] = dt.now().strftime("%d/%m/%y %H:%M:%S")
        elif artist['role'] == 'Bassist':
            artist['OVR'] = ovr_bass(artist)
            artist['timestamp'] = dt.now().strftime("%d/%m/%y %H:%M:%S")
        elif artist['role'] == 'Guitarrist':
            artist['OVR'] = ovr_guitar(artist)
            artist['timestamp'] = dt.now().strftime("%d/%m/%y %H:%M:%S")


    # carrega já existentes
    with open('artists.json', 'r') as arquivo:
        artists = json.load(arquivo)

    # cria set com nomes já existentes
    existing_names = {a['nome'] for a in artists}

    # adiciona apenas os que não são duplicados
    for new_artist in novos:
        if new_artist['nome'] not in existing_names:
            artists.append(new_artist)

    # salva de volta
    with open('artists.json', 'w') as arquivo:
        json.dump(artists, arquivo, indent=4)

    return artists


