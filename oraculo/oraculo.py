import streamlit as st
import random
import os
from datetime import datetime

st.set_page_config(page_title="oráculo das sombras", layout="centered", page_icon="👾")

# --- ESTILO VISUAL ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=UnifrakturCook:wght@700&display=swap');

        html, body, .stApp, * {
            background-color: #000000 !important;
            color: #39FF14 !important;
            font-family: 'UnifrakturCook', cursive !important;
        }

        .stTextInput > div > div > input {
            color: #39FF14;
            background-color: #111111;
            border: 1px solid #39FF14;
        }

        .stTextInput label {
            color: #39FF14;
        }

        .pergunta-container {
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .lado {
            width: 80px;
            height: 80px;
            margin: 0 20px;
        }

        .center-box {
            flex-grow: 1;
            max-width: 500px;
        }
    </style>
""", unsafe_allow_html=True)

# --- IMAGENS MÍSTICAS LATERAIS ---
img_esquerda = "https://i.imgur.com/2W5dUu2.png"  # sapo psicodélico
img_direita = "https://i.imgur.com/mkSfH6j.png"   # mago brisado

st.markdown("<h1 style='text-align: center;'>☠ Oráculo das Sombras ☠</h1>", unsafe_allow_html=True)
contador_path = "contador.txt"

# --- CONTADOR DE ALMAS ---
def carregar_contador():
    if not os.path.exists(contador_path):
        with open(contador_path, "w") as f:
            f.write("0")
    with open(contador_path, "r") as f:
        return int(f.read().strip())

def salvar_contador(valor):
    with open(contador_path, "w") as f:
        f.write(str(valor))

if "ultima_visita" not in st.session_state:
    st.session_state.ultima_visita = datetime.today().date()
    contador = carregar_contador() + 1
    salvar_contador(contador)
else:
    contador = carregar_contador()

st.markdown(f"<p style='text-align:center;'>🧍 {contador} almas já consultaram o Oráculo...</p>", unsafe_allow_html=True)

# --- HUMORES ---
humores = {
    "zombeteiro": lambda r: f"{r}  >:)",
    "fatalista": lambda r: f"{r}  (o fim está mais perto do que pensa...)",
    "críptico": lambda r: f"{r}  ¯\\_(ツ)_/¯",
    "frio": lambda r: f"{r}  [análise concluída]",
    "emocional": lambda r: f"{r}  ;-("
}
humor_hoje = random.choice(list(humores.keys()))

# --- BANCO DE RESPOSTAS ---
respostas_por_categoria = {
    "amor": [
        "O amor está doente, mas ainda respira.",
        "Ele não pensa mais em você... só quando chove.",
        "Seu coração lembra do que sua mente quer esquecer."
    ],
    "trabalho": [
        "Seu esforço sustenta um castelo de cartas.",
        "Você trabalha demais pra alguém que sonha tão pouco.",
        "A riqueza virá, mas ela cobra caro."
    ],
    "vida": [
        "Você já escolheu... só não percebeu ainda.",
        "Tudo que você sente é a vida te empurrando.",
        "Não há caminho certo — só mais escuridão com passos."
    ],
    "morte": [
        "Você não morre quando para de respirar... mas quando esquecem seu nome.",
        "O fim já começou — você só está atrasado.",
        "A morte te observa com tédio. Ainda não é sua vez."
    ],
    "tempo": [
        "O céu está instável... como suas emoções.",
        "Vai chover, sim. Mas só por dentro.",
        "O clima não decide. E você, já decidiu?"
    ],
    "data": [
        f"Hoje é {datetime.now().strftime('%A, %d de %B de %Y')}. Se isso importa...",
        "O tempo é uma prisão com perfume de rotina.",
        "Os dias passam. Você permanece?"
    ],
    "tecnologia": [
        "As máquinas vão dominar. Mas com paciência.",
        "Seu computador te odeia, mas com respeito.",
        "A IA observa. Ela já entendeu quem você é."
    ],
    "saude": [
        "Você não está quebrado. Só está no lugar errado.",
        "Até a escuridão tem pausas. Faça a sua.",
        "Seu corpo fala o que sua alma não ousa dizer."
    ],
    "desconhecido": [
        "Você fez a pergunta errada. E agora é tarde.",
        "O Oráculo não reconhece sua dúvida, mas reconhece você.",
        "Silêncio. A resposta virá em outro sonho."
    ]
}

# --- TRACKING DE RESPOSTAS USADAS ---
if "respostas_usadas" not in st.session_state:
    st.session_state.respostas_usadas = {categoria: [] for categoria in respostas_por_categoria}

# --- IDENTIFICADOR DE CATEGORIA ---
def identificar_categoria(pergunta):
    p = pergunta.lower()
    if any(x in p for x in ["amor", "relacionamento", "namoro", "ele", "ela"]): return "amor"
    if any(x in p for x in ["trabalho", "emprego", "carreira", "dinheiro", "grana"]): return "trabalho"
    if any(x in p for x in ["vida", "sentido", "caminho", "escolha"]): return "vida"
    if any(x in p for x in ["morte", "fim", "morrer", "acabar"]): return "morte"
    if any(x in p for x in ["chuva", "clima", "tempo", "vai chover"]): return "tempo"
    if any(x in p for x in ["hoje", "dia", "data", "semana"]): return "data"
    if any(x in p for x in ["computador", "tecnologia", "ia", "robô"]): return "tecnologia"
    if any(x in p for x in ["cansado", "ansiedade", "triste", "depress", "dor", "doença"]): return "saude"
    return "desconhecido"

# --- INTERFACE COM IMAGENS LATERAIS ---
st.markdown("<div class='pergunta-container'>", unsafe_allow_html=True)
st.markdown(f"<img class='lado' src='{img_esquerda}'>", unsafe_allow_html=True)
pergunta = st.text_input("✉️ Faça sua pergunta ao Oráculo:", key="pergunta")
st.markdown(f"<img class='lado' src='{img_direita}'>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- RESPOSTA ÚNICA POR CATEGORIA ---
if pergunta:
    categoria = identificar_categoria(pergunta)
    usadas = st.session_state.respostas_usadas[categoria]
    disponiveis = [r for r in respostas_por_categoria[categoria] if r not in usadas]

    if not disponiveis:
        usadas.clear()
        disponiveis = respostas_por_categoria[categoria][:]

    resposta = random.choice(disponiveis)
    st.session_state.respostas_usadas[categoria].append(resposta)
    resposta_final = humores[humor_hoje](resposta)

    st.markdown("---")
    st.markdown(f"❓ *{pergunta}*  \n☠ {resposta_final}")
