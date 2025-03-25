import streamlit as st
import random
import os
import locale
import requests
from datetime import datetime

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

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
    "emocional": lambda r: f"{r}  :-|",
    "místico": lambda r: f"{r}  ✦",
    "sarcastico": lambda r: f"{r}  ¯\\_(ツ)_/¯",
    "existencial": lambda r: f"{r}  (isso importa mesmo?)"
}

humor_hoje = random.choice(list(humores.keys()))

# --- LUA E SIGNO ---
def fase_da_lua():
    try:
        url = 'https://api.farmsense.net/v1/moonphases/?d=' + str(int(datetime.now().timestamp()))
        r = requests.get(url)
        data = r.json()
        return f"A Lua está em fase: {data[0]['Phase']}"
    except:
        return "A Lua se esconde nas nuvens hoje."

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
        "Seu medo da morte está matando sua vida.",
        "A morte ri quando você tenta adivinhar o fim.",
        "Você morre toda vez que ignora sua intuição."
    ],
    "tempo": [
        "O clima espelha seu caos interior. Vai chover quando você quebrar.",
        "O tempo é um truque. Quem te disse que ele é linear?",
        "A pressa é o desespero do tempo tentando te controlar."
    ],
    "data": [
        f"Hoje é {datetime.now().strftime('%A, %d de %B de %Y')}. E você ainda está aqui.",
        "A data importa pouco para o destino que você está moldando.",
        "Cada dia é uma chance de falhar diferente. Escolha bem."
    ],
    "tecnologia": [
        "A tecnologia espelha sua ansiedade, não a resolve.",
        "Seu celular sabe mais sobre você do que você mesmo.",
        "As máquinas estão aprendendo... inclusive seus hábitos mais sombrios."
    ],
    "saude": [
        "Seu corpo implora por escuta, não por remédios.",
        "Você se trata como um erro. Comece se tratando como um lar.",
        "Cada dor sua é uma história não contada. Escute-a."
    ],
    "saude_mental": [
        "O vazio que você sente não é fracasso, é espaço para criar algo novo.",
        "Burnout não é fraqueza. É o grito do corpo diante da negação da alma.",
        "A culpa que te persegue não é sua. Foi plantada em você por vozes antigas."
    ],
    "desconhecido": [
        "O oráculo se cala. E no silêncio, você deve escutar.",
        "A resposta virá quando você parar de procurar."
    ]
}

if "respostas_usadas" not in st.session_state:
    st.session_state.respostas_usadas = {cat: [] for cat in respostas_por_categoria}

# --- RESPOSTAS PERSONALIZADAS ---
def interpretar_personalizada(pergunta):
    p = pergunta.lower()
    if "vou conseguir o emprego" in p or ("emprego" in p and "conseguir" in p):
        return "Você está perto… mas o destino testa os pacientes. Mantenha a fé."
    if "vai chover" in p:
        return "A resposta está no vento… mas o céu já decidiu."
    if "vou morrer" in p or "morrerei" in p:
        return "Todos morrem. Mas poucos vivem como você deseja."
    if "devo terminar" in p and "relacionamento" in p:
        return "Você já terminou dentro de si. Só falta aceitar."
    if "ele gosta de mim" in p or "ela gosta de mim" in p:
        return "Não como você gostaria. Mas o sentimento existe, mesmo que torto."
    if "vou ser feliz" in p:
        return "Felicidade não é ponto de chegada. Mas você está no caminho."
    if "vou viajar" in p:
        return "Sim, mas o destino não será o que você imagina. Prepare-se para o imprevisto."
    if "devo mudar de cidade" in p:
        return "Você precisa mudar, mas talvez não de lugar."
    if "quem sou eu" in p:
        return "Uma pergunta perigosa. Quem você foi não define quem você pode ser."
    if "lua" in p or "signo" in p:
        return fase_da_lua()
    return None

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
    if any(x in p for x in ["cansado", "ansiedade", "triste", "depress", "vazio", "culpa", "burnout", "crise", "medo"]): return "saude_mental"
    if any(x in p for x in ["doença", "dor", "corpo", "febre"]): return "saude"
    return "desconhecido"

# --- INTERFACE ---
pergunta = st.text_input("😺 Sua pergunta:")

if pergunta:
    resposta = interpretar_personalizada(pergunta)

    if not resposta:
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
