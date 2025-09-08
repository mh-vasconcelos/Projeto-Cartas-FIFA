import streamlit as st
from func import load_artists, generate_card_svg
from generate_ovr import ovr
import json
import random

# --- App principal Streamlit ---
def main():
    ovr('artists_to_add.json')
    st.title("Cartas Musicais 🎸🎤🥁")
    st.subheader("Gere aleatoriamente uma carta de um artista foda no estilo Fifa Ultimate Team")

    # Botão para gerar artista aleatório
    if st.button("Gerar Carta Aleatória"):
        artists = load_artists()
        artist = random.choice(artists)
        st.write(f"### 🎶 {artist['nome']} — {artist['role']}")
        # 1. Crie 3 colunas. As duas das pontas servirão de espaçamento.
        col1, col2, col3 = st.columns(3)
        with col2:
          card_img = generate_card_svg(artist)
          st.image(card_img, caption="Sua carta gerada", use_column_width=False, width=350)

        # Salvar imagem temporária para download
        st.download_button(
        label="Baixar Carta SVG",
        data=card_img.encode('utf-8'),  # Ponto chave: A string SVG precisa ser codificada para bytes
        file_name=f"{artist['nome']}.svg", # Nome do arquivo que o usuário vai baixar
        mime="image/svg+xml"  # Informa ao navegador que é um arquivo SVG
        )

if __name__ == "__main__":
    main()
