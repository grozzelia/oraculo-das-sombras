import streamlit as st
import random

st.set_page_config(page_title="Oráculo das Sombras", layout="centered", page_icon="☠️")
st.markdown("<h1 style='text-align: center; color: #39FF14;'>☠️ Oráculo das Sombras ☠️</h1>", unsafe_allow_html=True)

pergunta = st.text_input("💭 Faça sua pergunta ao Oráculo:")

def interpretar(pergunta):
    pergunta = pergunta.lower()

    if any(p in pergunta for p in ["amor", "coração", "relacionamento", "ele", "ela"]):
        return random.choice([
            "🖤 Ele sente sua falta... mas já se perdeu no vazio.",
            "💔 O amor apodreceu no tempo. Só restam memórias.",
            "🕯️ Almas conectadas não se separam tão fácil... mas sofrem juntas."
        ])
    elif any(p in pergunta for p in ["trabalho", "emprego", "carreira"]):
        return random.choice([
            "📉 Você está preso a um ciclo. Mudar dói, mas ficar corrói.",
            "🪓 Sua carreira sangra em silêncio."
        ])
    elif any(p in pergunta for p in ["dinheiro", "finanças"]):
        return random.choice([
            "💰 A riqueza é uma maldição disfarçada de desejo.",
            "💸 Nem todo ouro brilha. Às vezes... ele grita."
        ])
    elif any(p in pergunta for p in ["vida", "sentido", "caminho"]):
        return random.choice([
            "🌌 A vida não tem respostas. Apenas repetições.",
            "⚰️ A dúvida que você sente... é a resposta tentando te proteger."
        ])
    elif any(p in pergunta for p in ["morte", "fim"]):
        return random.choice([
            "☠️ A morte não responde perguntas... ela coleta.",
            "🖤 Já começou. Você só ainda não percebeu."
        ])
    else:
        return random.choice([
            "⛓️ O Oráculo se recusa a responder. Ainda.",
            "💀 Você fez a pergunta errada. E agora é tarde.",
        ])

if pergunta:
    resposta = interpretar(pergunta)
    st.markdown(f"<div style='text-align:center; font-size:20px; color:#39FF14;'>{resposta}</div>", unsafe_allow_html=True)
