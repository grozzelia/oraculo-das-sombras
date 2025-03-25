import streamlit as st
import random
import os
from datetime import datetime

# --- CONFIGURAÇÕES INICIAIS ---
st.set_page_config(page_title="Oráculo das Sombras", layout="centered", page_icon="☠️")
st.markdown(
    """
    <style>
        body {
            background-color: #0a0a0a;
        }
        .stTextInput > div > div > input {
            color: #39FF14;
            background-color: #111;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- FUNÇÕES ---
def carregar_contador():
    if not os.path.exists("contador.txt"):
        with open("contador.txt", "w") as f:
            f.write("0")
    with open("contador.txt", "r") as f:
        return int(f.read().strip())

def salvar_contador(valor):
    with open("contador.txt", "w") as f:
        f.write(str(valor))

def interpretar(pergunta):
    pergunta = pergunta.lower().strip()

    if any(p in pergunta for p in ["amor", "coração", "relacionamento", "ele", "ela"]):
        return random.choice([
            "🖤 Ele sente sua falta... mas já se perdeu no vazio.",
            "💔 O amor apodreceu no tempo. Só restam memórias.",
            "🕯️ Almas conectadas não se separam tão fácil... mas sofrem juntas.",
        ])
    elif any(p in pergunta for p in ["trabalho", "emprego", "carreira"]):
        return random.choice([
            "📉 Você está preso a um ciclo. Mudar dói, mas ficar corrói.",
            "🪓 Sua carreira sangra em silêncio.",
        ])
    elif any(p in pergunta for p in ["dinheiro", "finanças", "grana"]):
        return random.choice([
            "💰 A riqueza é uma maldição disfarçada de desejo.",
            "💸 Nem todo ouro brilha. Às vezes... ele grita.",
        ])
    elif any(p in pergunta for p in ["vida", "sentido", "caminho"]):
        return random.choice([
            "🌌 A vida não tem respostas. Apenas repetições.",
            "⚰️ A dúvida que você sente... é a resposta tentando te proteger.",
        ])
    elif any(p in pergunta for p in ["morte", "fim", "morr"]):
        return random.choice([
            "☠️ A morte não responde perguntas... ela coleta.",
            "🖤 Já começou. Você só ainda não percebeu.",
        ])
    else:
        return random.choice([
            "⛓️ O Oráculo se recusa a responder. Ainda.",
            "💀 Você fez a pergunta errada. E agora é tarde.",
        ])

# --- CONTADOR DE ALMAS ---
if "ultima_visita" not in st.session_state:
    st.session_state.ultima_visita = datetime.today().date()
    contador = carregar_contador()
    contador += 1
    salvar_contador(contador)
else:
    contador = carregar_contador()

# --- INTERFACE ---
st.markdown("<h1 style='text-align: center; color: #39FF14;'>☠️ Oráculo das Sombras ☠️</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#777;'>🧍‍♂️ {contador} almas já consultaram o Oráculo...</p>", unsafe_allow_html=True)

pergunta = st.text_input("💭 Faça sua pergunta ao Oráculo:")

if "historico" not in st.session_state:
    st.session_state.historico = []

if pergunta:
    resposta = interpretar(pergunta)
    st.session_state.historico.append((pergunta, resposta))
    st.markdown("---")

    for p, r in reversed(st.session_state.historico):
        st.markdown(f"❓ *{p}*  \n☠️ **{r}**")
