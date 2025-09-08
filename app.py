import streamlit as st
from func import load_artists, generate_card_mvp
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
          card_img = generate_card_mvp(artist)
          st.image(card_img, caption="Sua carta gerada", use_column_width=False, width=350)

        # Salvar imagem temporária para download
        card_img.save("temp_card.png")
        with open("temp_card.png", "rb") as f:
            st.download_button(
                label="⬇️ Baixar Carta",
                data=f,
                file_name=f"{artist['nome'].replace(' ', '_')}.png",
                mime="image/png"
            )

if __name__ == "__main__":
    main()
