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

    # -----------------------
    # Inicialização do session_state (adicionado)
    # -----------------------
    # Banda persistida (lista de artistas), SVGs e hrefs base64
    if "band_artists" not in st.session_state:
        st.session_state["band_artists"] = None
    if "band_svgs" not in st.session_state:
        st.session_state["band_svgs"] = None
    if "band_hrefs" not in st.session_state:
        st.session_state["band_hrefs"] = None

    # Carta única persistida (artista), svg e href
    if "single_artist" not in st.session_state:
        st.session_state["single_artist"] = None
    if "single_svg" not in st.session_state:
        st.session_state["single_svg"] = None
    if "single_href" not in st.session_state:
        st.session_state["single_href"] = None
    # -----------------------
    # Fim inicialização session_state
    # -----------------------

    # 2. SEPARAÇÃO EM CONTÊINERES
    
    # Contêiner 1: Cabeçalho da aplicação
    with st.container(border=True):
        # A função ovr() estava aqui, mantive o lugar.
        st.title("Cartas Musicais 🎸🎤🥁")
        st.subheader("Gere aleatoriamente uma carta de um músico no estilo Fifa Ultimate Team")
    st.markdown("<br>", unsafe_allow_html=True)

    # Contêiner 2: Gerador de Cartas para banda
    with st.container(border=True):
        st.header("Gerar Banda")   
        # Botão para gerar artista aleatório
        if st.button("Gerar Cartas Aleatórias"):
            artists = load_artists()
            banda = pick_band(artists=artists)

            # Gera e salva no session_state os SVGs e hrefs (base64)
            svgs = []
            hrefs = []
            for a in banda:
                svg = generate_card_svg(a)
                svgs.append(svg)
                b64 = base64.b64encode(svg.encode('utf-8')).decode('ascii')
                hrefs.append(f"data:image/svg+xml;base64,{b64}")

            st.session_state["band_artists"] = banda
            st.session_state["band_svgs"] = svgs
            st.session_state["band_hrefs"] = hrefs

        # Sempre renderiza a banda se estiver persistida no session_state
        if st.session_state.get("band_artists"):
            banda = st.session_state["band_artists"]
            svgs = st.session_state["band_svgs"] or []
            # Colunas para centralizar a carta
            col1, col2, col3, col4 = st.columns([3, 3, 3, 3])

            # Renderiza cada coluna a partir dos SVGs persistidos (se existirem)
            with col1:
                card_img = svgs[0] if len(svgs) > 0 else generate_card_svg(banda[0])
                st.image(card_img)
            with col2:
                card_img = svgs[1] if len(svgs) > 1 else generate_card_svg(banda[1])
                st.image(card_img)

            with col3:
                card_img = svgs[2] if len(svgs) > 2 else generate_card_svg(banda[2])
                st.image(card_img)
            with col4:
                card_img = svgs[3] if len(svgs) > 3 else generate_card_svg(banda[3])
                st.image(card_img)
              
    # Container 3: gerador de carta única para download
    with st.container(border=True):
      st.header("Gerar o Artista")
      
      # Botão para gerar artista aleatório
      if st.button("Gerar Carta Aleatória"):
          artists = load_artists()
          artist = random.choice(artists)
          
          # Gera SVG e salva no session_state
          svg = generate_card_svg(artist)
          b64 = base64.b64encode(svg.encode('utf-8')).decode('ascii')
          href_data = f"data:image/svg+xml;base64,{b64}"

          st.session_state["single_artist"] = artist
          st.session_state["single_svg"] = svg
          st.session_state["single_href"] = href_data
          
      # Sempre renderiza a carta única se existir no session_state
      if st.session_state.get("single_artist"):
          artist = st.session_state["single_artist"]
          svg_to_show = st.session_state.get("single_svg")
          href_data = st.session_state.get("single_href")

          st.write(f"### 🎶 {artist['nome']} — {artist['role']}")
          
          # Colunas para centralizar a carta
          col1, col2, col3 = st.columns([1, 4, 1])
          
          # Coluna do meio maior
          with col2:
              card_img = svg_to_show
              st.image(card_img)
            
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
