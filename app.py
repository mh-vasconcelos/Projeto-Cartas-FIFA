import streamlit as st
from func import load_artists, generate_card_svg, pick_band
from card_code import DARK_MODE_CSS
import base64
import random


def main():
    # 1. CONFIGURAÇÃO DA PÁGINA: MODO DARK
    st.set_page_config(
        page_title="Cartas Musicais",
        page_icon="🎸",
        layout="centered", # ou "wide"
        initial_sidebar_state="auto",
        menu_items=None
    )
    st.markdown(DARK_MODE_CSS, unsafe_allow_html=True)

    # 2. SEPARAÇÃO EM CONTÊINERES
    
    # Contêiner 1: Cabeçalho da aplicação
    with st.container(border=True):
        # A função ovr() estava aqui, mantive o lugar.
        st.title("Cartas Musicais 🎸🎤🥁")
        st.subheader("Gere aleatoriamente uma carta de um artista foda no estilo Fifa Ultimate Team")
    st.markdown("<br>", unsafe_allow_html=True)

    # Contêiner 2: Gerador de Cartas para banda
    with st.container(border=True):
        st.header("Gerar Banda")   
        # Botão para gerar artista aleatório
        if st.button("Gerar Cartas Aleatórias", use_container_width=True):
            artists = load_artists()
            banda = pick_band(artists=artists)
            st.write(f"### 🎶 Sua banda é:")
            
            # Colunas para centralizar a carta
            col1, col2, col3, col4 = st.columns([3, 3, 3, 3]) # Coluna do meio maior
            with col1:
              card_img = generate_card_svg(banda[0])
              st.image(card_img, use_column_width=True)
              svg_str = card_img  # ou svg, conforme seu nome de variável
              b64 = base64.b64encode(svg_str.encode('utf-8')).decode('ascii')
              href_data = f"data:image/svg+xml;base64,{b64}"
            with col2:
              card_img = generate_card_svg(banda[1])
              st.image(card_img, use_column_width=True)
              svg_str = card_img  # ou svg, conforme seu nome de variável
              b64 = base64.b64encode(svg_str.encode('utf-8')).decode('ascii')
              href_data = f"data:image/svg+xml;base64,{b64}"

            with col3:
              card_img = generate_card_svg(banda[2])
              st.image(card_img, use_column_width=True)
              svg_str = card_img  # ou svg, conforme seu nome de variável
              b64 = base64.b64encode(svg_str.encode('utf-8')).decode('ascii')
              href_data = f"data:image/svg+xml;base64,{b64}"

            with col4:
              card_img = generate_card_svg(banda[3])
              st.image(card_img, use_column_width=True)
              svg_str = card_img  # ou svg, conforme seu nome de variável
              b64 = base64.b64encode(svg_str.encode('utf-8')).decode('ascii')
              href_data = f"data:image/svg+xml;base64,{b64}"
              
    # Container 3: gerador de carta única para download
    with st.container(border=True):
      st.header("Gerar o Artista")
      
      # Botão para gerar artista aleatório
      if st.button("Gerar Carta Aleatória", use_container_width=True):
          artists = load_artists()
          artist = random.choice(artists)
          
          st.write(f"### 🎶 {artist['nome']} — {artist['role']}")
          
          # Colunas para centralizar a carta
          col1, col2, col3 = st.columns([1, 4, 1])
          
          # Coluna do meio maior
          with col2:
              card_img = generate_card_svg(artist)
              svg_str = card_img
              st.image(card_img, caption="Sua carta gerada", use_column_width=True)
              b64 = base64.b64encode(svg_str.encode('utf-8')).decode('ascii')
              href_data = f"data:image/svg+xml;base64,{b64}"

            
          download_button_html = f'''
          <div style="display:flex; justify-content:center; margin-top:12px;">
            <a download="{(artist.get('nome') or 'card').replace(' ','_')}.svg"
              href="{href_data}"
              style="
                  display:inline-block;
                  padding:14px 22px;
                  background: linear-gradient(90deg,#f59e0b,#facc15);
                  color:#0a1526 !important;
                  font-weight:700;
                  text-decoration:none;
                  border-radius:8px;
                  box-shadow: 0 6px 16px rgba(2,6,23,0.6);
                  width: 100%;
                  text-align:center;
              ">
              Baixar Carta SVG
            </a>
          </div>
          '''
          st.markdown(download_button_html, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
