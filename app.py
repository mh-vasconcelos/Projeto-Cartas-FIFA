import streamlit as st
from func import load_artists, generate_card_svg
from generate_ovr import ovr
import json
import random
from card_code import DARK_MODE_CSS
import base64
from urllib.parse import quote

# --- App principal Streamlit ---
# def main():
#     with st.container():
#       ovr('artists_to_add.json')
#       st.title("Cartas Musicais 🎸🎤🥁")
#       st.subheader("Gere aleatoriamente uma carta de um artista foda no estilo Fifa Ultimate Team")

#     # Botão para gerar artista aleatório
#     if st.button("Gerar Carta Aleatória"):
#         artists = load_artists()
#         artist = random.choice(artists)
#         st.write(f"### 🎶 {artist['nome']} — {artist['role']}")
#         # 1. Crie 3 colunas. As duas das pontas servirão de espaçamento.
#         col1, col2, col3 = st.columns(3)
#         with col2:
#           card_img = generate_card_svg(artist)
#           st.image(card_img, caption="Sua carta gerada", use_column_width=False, width=350)

#         # Salvar imagem temporária para download
#         st.download_button(
#         label="Baixar Carta SVG",
#         data=card_img.encode('utf-8'),  # Ponto chave: A string SVG precisa ser codificada para bytes
#         file_name=f"{artist['nome']}.svg", # Nome do arquivo que o usuário vai baixar
#         mime="image/svg+xml"  # Informa ao navegador que é um arquivo SVG
#         )


def main():
    # 1. CONFIGURAÇÃO DA PÁGINA: MODO DARK
    # Deve ser o primeiro comando Streamlit do seu script.
    st.set_page_config(
        page_title="Cartas Musicais",
        page_icon="🎸",
        layout="centered", # ou "wide"
        initial_sidebar_state="auto",
        menu_items=None
    )
    st.markdown(DARK_MODE_CSS, unsafe_allow_html=True)

    # Forçando o tema escuro (opcional, 'auto' respeita a preferência do sistema)
    # st.config.set_option('theme.base', 'dark') # Forma antiga, agora use set_page_config

    # 2. SEPARAÇÃO EM CONTÊINERES
    
    # Contêiner 1: Cabeçalho da aplicação
    with st.container(border=True):
        # A função ovr() estava aqui, mantive o lugar.
        ovr('artists_to_add.json')
        st.title("Cartas Musicais 🎸🎤🥁")
        st.subheader("Gere aleatoriamente uma carta de um artista foda no estilo Fifa Ultimate Team")

    # Adiciona um espaço vertical para melhor legibilidade
    st.markdown("<br>", unsafe_allow_html=True)

    # Contêiner 2: Gerador de Cartas
    with st.container(border=True):
        st.header("Gerador")
        # Botão para gerar artista aleatório
        if st.button("Gerar Carta Aleatória", use_container_width=True):
            artists = load_artists()
            artist = random.choice(artists)
            
            st.write(f"### 🎶 {artist['nome']} — {artist['role']}")
            
            # Colunas para centralizar a carta
            col1, col2, col3 = st.columns([1, 4, 1]) # Coluna do meio maior
            with col2:
              card_img = generate_card_svg(artist)
              st.image(card_img, use_column_width=True)
              svg_str = card_img  # ou svg, conforme seu nome de variável
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
