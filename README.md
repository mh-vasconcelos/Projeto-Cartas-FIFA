# Projeto-Cartas-FIFA
🎸 Rock Ultimate Cards

Cartinhas digitais no estilo EA Sports Ultimate Team, mas para músicos de rock.
Cada artista recebe atributos como Energia, Técnica, Carisma, etc, e uma nota geral (OVR).
O objetivo é gerar cartas estilizadas que podem ser visualizadas na web, baixadas como PNG e até usadas para montar bandas dos sonhos no futuro.

## 📌 Objetivo do Projeto

Este é um projeto de entretenimento para os fãs de música (e um pouco de futebol também) não que acrescenta uma camada de diversão para fãs de música e colecionadores digitais.

## 🚀 MVP (Primeira Versão)

O MVP se concentra em três etapas principais:

- Template JSON com informações dos artistas (nome, atributos, país, role, etc).

- Script Python que calcula o Overall (OVR) do artista a partir de pesos definidos para cada papel (vocalista, guitarrista, baterista, baixista), além de usar um RPA para buscar a imagem do artista no Google imagems para preencher

- Front-end em Streamlit, que permite gerar cartas aleatórias a partir dos dados e exibi-las como imagens estilizadas.

### Requisitos funcionais:
- [x]  Funcionalidade para gerar uma banda aleatória, separada com baixista, baterista, vocalista e guitarrista
- [x]  Funcionalidade para gerar uma carta única com opção de download
- [x]  RPA para pegar as imagens automaticamente com base no nome do artista
- [x]  Separação lógica para destacar a banda do músico, de modo a gerar diferentes cartas para um mesmo músico com notas diferentes
- [ ]  Separação lógica de um músico que toca diferentes instrumentos. Aqui, podemos até gerar cartas do mesmo músico na geração da banda (sendo um power trio, por exemplo), desde que elaboremos corretamente as regras no código, para evitar uma banda com apenas dois integrantes, por exemplo. As notas também seriam de acordo com o instrumento.
- [ ]  Gerar Overall para a banda, de acordo com alguns critérios, por exemplo, músicos da mesma banda, artistas da mesmo país, etc.
- [ ]  Criar botão de compartilhar

### Requisitos não-funcionais
- [x]  Estabelecer consistência de estado (session state) para que o usuário não perca informações dos dados

### Critérios de avaliação
Cada artista tem 6 atributos (ENA, COM, ARR, TEC, CON, CAR).
O OVR (overall) é uma média ponderada desses atributos — os pesos mudam conforme a função do artista (vocalista, guitarrista, baixista, baterista).
As descrições abaixo explicam o significado de cada atributo no contexto de cada função e apresentam os pesos sugeridos.
```json
{
  "nome": "Exemplo Nome",
  "role": "Singer",        // Singer, Guitarrist, Bassist, Drummer
  "country": "Country",
  "ENA": 85,
  "COM": 90,
  "ARR": 80,
  "TEC": 88,
  "CON": 82,
  "CAR": 91,
  "OVR": 0,                // calculado depois pelo script generated_info.py
  "band": "Nome da Banda",
  "img": (RPA),
  "timestamp": "0"
}
```

#### Critérios (definições gerais)

- ENA (Energia) — presença de palco e intensidade nas performances.

- COM (Composição) — habilidade de compor melodias/linhas/ideias marcantes.

- ARR (Arranjo) — sensibilidade para harmonias, texturas e construção do arranjo.

- TEC (Técnica) — execução do instrumento/voz (precisão, controle, habilidades técnicas).

- CON (Consistência) — manutenção de qualidade ao longo da carreira.

- CAR (Carisma) — impacto cultural, presença, imagem pública.


## 🛠️ Tecnologias Utilizadas

- Python 3.10+

- Streamlit → interface web rápida.

- Pandas → manipulação de dados.

- JSON → armazenamento de dados dos artistas.

- SVG → template visual das cartas.