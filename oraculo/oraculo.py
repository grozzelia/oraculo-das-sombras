import tkinter as tk
import random

def interpretar_pergunta(pergunta):
    pergunta = pergunta.lower()

    if "amor" in pergunta or "coração" in pergunta or "relacionamento" in pergunta or "ele" in pergunta or "ela" in pergunta:
        return random.choice([
            "🖤 Ele sente sua falta... mas já se perdeu no vazio.",
            "💔 O amor apodreceu no tempo. Só restam memórias.",
            "🕯️ Almas conectadas não se separam tão fácil... mas sofrem juntas.",
            "🔗 Ela pensa em você... mas não da forma que você deseja."
        ])

    elif "trabalho" in pergunta or "emprego" in pergunta or "carreira" in pergunta:
        return random.choice([
            "📉 Você está preso a um ciclo. Mudar dói, mas ficar corrói.",
            "🕰️ O tempo no trabalho consome a alma. Escolha o menor tormento.",
            "🔧 As engrenagens da sua vida precisam ser trocadas.",
            "🪓 Sua carreira sangra em silêncio. O corte virá de onde menos espera."
        ])

    elif "dinheiro" in pergunta or "finanças" in pergunta or "riqueza" in pergunta:
        return random.choice([
            "💰 A riqueza é uma maldição disfarçada de desejo.",
            "🩸 Cuidado com o preço que você paga por querer mais.",
            "🧾 Suas finanças estão marcadas. Equilibre antes que te cobrem.",
            "💸 Nem todo ouro brilha. Às vezes... ele grita."
        ])

    elif "vida" in pergunta or "sentido" in pergunta or "caminho" in pergunta:
        return random.choice([
            "🌌 A vida não tem respostas. Apenas repetições.",
            "🧿 O caminho está à sua frente. Você que não quer ver.",
            "📿 O sentido? Sobrevivência. O resto é delírio.",
            "⚰️ A dúvida que você sente... é a resposta tentando te proteger."
        ])

    elif "morte" in pergunta or "fim" in pergunta:
        return random.choice([
            "🕳️ Ela está mais próxima do que você imagina.",
            "⚰️ O fim não avisa. Só observa.",
            "☠️ A morte não responde perguntas... ela coleta.",
            "🖤 Já começou. Você só ainda não percebeu."
        ])

    else:
        return random.choice([
            "⛓️ O Oráculo se recusa a responder. Ainda.",
            "💀 Você fez a pergunta errada. E agora é tarde.",
            "🌫️ O destino está obscurecido. Tente de novo. Ou não.",
            "🧩 O caos não entende perguntas claras. Faça de novo, com medo."
        ])

def consultar_oraculo():
    pergunta = entrada.get()
    if pergunta.strip() == "":
        resultado["text"] = "🩸 O vazio não tem resposta. Nem perdão."
    else:
        resposta = interpretar_pergunta(pergunta)
        resultado["text"] = f"💀 O Oráculo responde:\n\n{resposta}"

# Interface Gráfica
janela = tk.Tk()
janela.title("Oráculo das Sombras")
janela.geometry("500x330")
janela.config(bg="#0a0a0a")  # fundo sombrio

FONTE_GOTICA = ("Lucida Console", 12, "bold")
COR_VERDE_NEON = "#39FF14"

titulo = tk.Label(
    janela,
    text="☠️ Oráculo das Sombras ☠️",
    font=("Lucida Console", 16, "bold"),
    fg=COR_VERDE_NEON,
    bg="#0a0a0a"
)
titulo.pack(pady=10)

entrada = tk.Entry(
    janela,
    font=FONTE_GOTICA,
    width=50,
    bg="#1a1a1a",
    fg=COR_VERDE_NEON,
    insertbackground=COR_VERDE_NEON
)
entrada.pack(pady=10)

botao = tk.Button(
    janela,
    text="Invocar o Oráculo",
    font=FONTE_GOTICA,
    bg="#003300",
    fg=COR_VERDE_NEON,
    activebackground="#004d00",
    command=consultar_oraculo
)
botao.pack(pady=10)

resultado = tk.Label(
    janela,
    text="",
    font=("Lucida Console", 11),
    fg=COR_VERDE_NEON,
    bg="#0a0a0a",
    wraplength=460,
    justify="center"
)
resultado.pack(pady=20)

janela.mainloop()
