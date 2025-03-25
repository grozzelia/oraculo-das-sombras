import streamlit as st
import random
import os
from datetime import datetime

st.set_page_config(page_title="oráculo das sombras", layout="centered", page_icon="👾")

# --- ESTILO VISUAL ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=MedievalSharp&display=swap');

        html, body, .stApp {
            background-color: #3e2c41 !important;
            color: #baffc9 !important;
            font-family: 'Courier New' !important;
        }

        h1 {
            font-family: 'MedievalSharp', cursive !important;
            font-size: 40px !important;
            text-align: center;
            margin-bottom: 0;
            color: #baffc9 !important;
            text-shadow: 1px 1px 2px black;
        }

        .stTextInput > div > div > input {
            color: #baffc9 !important;
            background-color: #4e3b53 !important;
            border: 1px solid #baffc9 !important;
            font-size: 18px !important;
            font-family: 'Courier New' !important;
        }

        .stTextInput label {
            color: #baffc9 !important;
            font-size: 18px !important;
            font-family: 'Courier New' !important;
            text-shadow: 1px 1px 2px black;
        }

        .block-container {
            padding-top: 2rem;
        }

        .stMarkdown {
            font-size: 20px;
            font-family: 'Courier New' !important;
            text-shadow: 1px 1px 2px black;
        }

        .viewerBadge_container__1QSob,
        .stStatusWidget,
        header,
        .css-18ni7ap {
            background-color: #3e2c41 !important;
            color: #baffc9 !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- TÍTULO ---
st.markdown("<h1>👾 oráculo das sombras 👾</h1>", unsafe_allow_html=True)

# --- CONTADOR DE ALMAS ---
contador_path = "contador.txt"

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

st.markdown(f"""
    <div style='text-align:center; font-size:18px; margin-top:0px; margin-bottom:30px'>
        👻 {contador} almas já consultaram o oráculo...
    </div>
""", unsafe_allow_html=True)

# --- HUMORES ---
humores = {
    "zombeteiro": lambda r: f"{r}  >:)",
    "fatalista": lambda r: f"{r}  (não adianta fugir...)",
    "críptico": lambda r: f"{r}  :::",
    "frio": lambda r: f"{r}  [análise encerrada]",
    "emocional": lambda r: f"{r}  :-|"
}
humor_hoje = random.choice(list(humores.keys()))

# --- RESPOSTAS POR CATEGORIA ---
respostas_por_categoria = {
    "amor": [
        "O amor que você busca está na sombra de quem você costumava ser.",
        "O desejo está contaminado. Purifique-se antes de pedir reciprocidade.",
        "Ele pensa, mas não com afeto. Apenas com saudade do controle.",
        "Você ama mais a ideia do que o real. E o real já partiu.",
        "Elx observa de longe, mas o coração está em outro tempo."
    ],
    "trabalho": [
        "Você não trabalha: você sobrevive mascarado de produtividade.",
        "A promoção que você deseja não comprará sua paz.",
        "A riqueza está próxima, mas virá travestida de sacrífio.",
        "Seu talento está sendo vendido a preço de banana pela sua zona de conforto."
    ],
    "vida": [
        "Tudo está conectado, mas você insiste em olhar só pro que brilha.",
        "A vida quer te empurrar pra uma porta... que você está com medo de abrir.",
        "Você é feito(a) de repetições, mas uma pequena quebra pode te libertar.",
        "A escolha certa é aquela que assusta e atrai ao mesmo tempo."
    ],
    "morte": [
        "A morte está entediada. Não você.",
        "Seu medo da morte está matando sua vida."
    ],
    "tempo": [
        "O clima espelha seu caos interior. Vai chover quando você quebrar."
    ],
    "data": [
        f"Hoje é {datetime.now().strftime('%A, %d de %B de %Y')}. E você ainda está aqui.",
        "A data importa pouco para o destino que você está moldando."
    ],
    "tecnologia": [
        "A tecnologia espelha sua ansiedade, não a resolve.",
        "Seu celular sabe mais sobre você do que sua família."
    ],
    "saude": [
        "Seu corpo implora por escuta, não por remédios.",
        "Você se trata como um erro. Comece se tratando como um lar."
    ],
    "desconhecido": [
        "O oráculo se cala. E no silêncio, você deve escutar.",
        "A resposta virá quando você parar de procurar."
    ]
}

# --- TRACKING DE RESPOSTAS USADAS ---
if "respostas_usadas" not in st.session_state:
    st.session_state.respostas_usadas = {cat: [] for cat in respostas_por_categoria}

# --- CATEGORIZADOR DE PERGUNTA ---
def identificar_categoria(pergunta):
    p = pergunta.lower()
    if any(x in p for x in ["amor", "relacionamento", "namoro", "ele", "ela"]): return "amor"
    if any(x in p for x in ["trabalho", "emprego", "carreira", "dinheiro", "grana", "rico", "rica"]): return "trabalho"
    if any(x in p for x in ["vida", "sentido", "caminho", "escolha"]): return "vida"
    if any(x in p for x in ["morte", "fim", "morrer", "acabar"]): return "morte"
    if any(x in p for x in ["chuva", "clima", "tempo", "vai chover"]): return "tempo"
    if any(x in p for x in ["hoje", "dia", "data", "semana"]): return "data"
    if any(x in p for x in ["computador", "tecnologia", "ia", "robô"]): return "tecnologia"
    if any(x in p for x in ["cansado", "ansiedade", "triste", "depress", "dor", "doença"]): return "saude"
    return "desconhecido"

# --- INTERFACE ---
pergunta = st.text_input("👹 Sua pergunta:")

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
    st.markdown(f"{resposta_final}")
