import streamlit as st
import random
import os
from datetime import datetime

# 🛠️ Precisa ser o PRIMEIRO comando visual
st.set_page_config(page_title="Oráculo das Sombras", layout="centered", page_icon="☠️")

# 🌑 Estilo completo dark (inclusive a barra branca)
st.markdown(
    """
    <style>
        html, body, .stApp {
            background-color: #000000;
        }
        h1, p, label, .stMarkdown {
            color: #39FF14 !important;
        }
        .stTextInput > div > div > input {
            color: #39FF14;
            background-color: #111111;
            border: 1px solid #39FF14;
        }
        .stTextInput label {
            color: #39FF14;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎭 Roleta de humores
humores = {
    "zombeteiro": lambda r: f"{r}  >:D",
    "fatalista": lambda r: f"{r}  (o fim está mais perto do que pensa...)",
    "críptico": lambda r: f"{r}  ¯\\_(ツ)_/¯",
    "frio": lambda r: f"{r}  [análise concluída]",
    "emocional": lambda r: f"{r}  ;-("
}
humor_hoje = random.choice(list(humores.keys()))

# 📊 Contador de almas
def carregar_contador():
    if not os.path.exists("contador.txt"):
        with open("contador.txt", "w") as f:
            f.write("0")
    with open("contador.txt", "r") as f:
        return int(f.read().strip())

def salvar_contador(valor):
    with open("contador.txt", "w") as f:
        f.write(str(valor))

# 🔮 Interpretador de perguntas com categorias expandidas
def interpretar(pergunta):
    p = pergunta.lower().strip()

    if any(x in p for x in ["amor", "relacionamento", "namoro", "ele", "ela"]):
        base = random.choice([
            "O amor está doente, mas ainda respira.",
            "Ele não pensa mais em você... só quando chove.",
            "Seu coração lembra do que sua mente quer esquecer."
        ])
    elif any(x in p for x in ["trabalho", "emprego", "carreira", "dinheiro", "grana"]):
        base = random.choice([
            "Seu esforço sustenta um castelo de cartas.",
            "Você trabalha demais pra alguém que sonha tão pouco.",
            "A riqueza virá, mas ela cobra caro."
        ])
    elif any(x in p for x in ["vida", "sentido", "caminho", "escolha"]):
        base = random.choice([
            "Você já escolheu... só não percebeu ainda.",
            "Tudo que você sente é a vida te empurrando.",
            "Não há caminho certo — só mais escuridão com passos."
        ])
    elif any(x in p for x in ["morte", "fim", "morrer", "acabar"]):
        base = random.choice([
            "Você não morre quando para de respirar... mas quando esquecem seu nome.",
            "O fim já começou — você só está atrasado.",
            "A morte te observa com tédio. Ainda não é sua vez."
        ])
    elif any(x in p for x in ["chuva", "clima", "tempo", "vai chover"]):
        base = random.choice([
            "O céu está instável... como suas emoções.",
            "Vai chover, sim. Mas só por dentro.",
            "O clima não decide. E você, já decidiu?"
        ])
    elif any(x in p for x in ["hoje", "dia", "data", "semana"]):
        base = random.choice([
            f"Hoje é {datetime.now().strftime('%A, %d de %B de %Y')}. Se isso importa...",
            "O tempo é uma prisão com perfume de rotina.",
            "Os dias passam. Você permanece?"
        ])
    elif any(x in p for x in ["computador", "tecnologia", "ia", "robô"]):
        base = random.choice([
            "As máquinas vão dominar. Mas com paciência.",
            "Seu computador te odeia, mas com respeito.",
            "A IA observa. Ela já entendeu quem você é."
        ])
    elif any(x in p for x in ["cansado", "ansiedade", "triste", "depress", "dor", "doença"]):
        base = random.choice([
            "Você não está quebrado. Só está no lugar errado.",
            "Até a escuridão tem pausas. Faça a sua.",
            "Seu corpo fala o que sua alma não ousa dizer."
        ])
    else:
        base = random.choice([
            "Você fez a pergunta errada. E agora é tarde.",
            "O Oráculo não reconhece sua dúvida, mas reconhece você.",
            "⛓️ Silêncio. A resposta virá em outro sonho."
        ])

    return humores[humor_hoje](base)

# 🎯 Contador de almas por sessão
if "ultima_visita" not in st.session_state:
    st.session_state.ultima_visita = datetime.today().date()
    contador = carregar_contador()
    contador += 1
    salvar_contador(contador)
else:
    contador = carregar_contador()

# 🧙 Interface principal
st.markdown("<h1 style='text-align: center; color: #39FF14;'>☠ Oráculo das Sombras ☠</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#777;'>🧍 {contador} almas já consultaram o Oráculo...</p>", unsafe_allow_html=True)

pergunta = st.text_input("✉️ Faça sua pergunta ao Oráculo:")

if "historico" not in st.session_state:
    st.session_state.historico = []

if pergunta:
    resposta = interpretar(pergunta)
    st.session_state.historico.append((pergunta, resposta))
    st.markdown("---")
    for p, r in reversed(st.session_state.historico):
        st.markdown(f"❓ *{p}*  \n☠ {r}")
