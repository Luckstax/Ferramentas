import os
import platform
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox


# =========================
# LÓGICA DE SISTEMA
# =========================

def sistema_suportado():
    return platform.system() == "Windows"


def executar_comando(acao: str, segundos: int):
    if acao == "desligar":
        os.system(f"shutdown /s /t {segundos}")
    elif acao == "reiniciar":
        os.system(f"shutdown /r /t {segundos}")


def cancelar_desligamento():
    os.system("shutdown /a")


# =========================
# LÓGICA DE TEMPO
# =========================

def segundos_por_contagem(horas: int, minutos: int) -> int:
    return horas * 3600 + minutos * 60


def segundos_ate_horario(hora_str: str) -> int:
    agora = datetime.now()
    alvo = datetime.strptime(hora_str, "%H:%M").replace(
        year=agora.year,
        month=agora.month,
        day=agora.day
    )

    if alvo <= agora:
        alvo += timedelta(days=1)

    return int((alvo - agora).total_seconds())


# =========================
# INTERFACE
# =========================

def executar():
    if not sistema_suportado():
        messagebox.showerror("Erro", "Sistema operacional não suportado.")
        return

    acao = acao_var.get()
    modo = modo_var.get()

    try:
        if modo == "contagem":
            horas = int(entry_horas.get())
            minutos = int(entry_minutos.get())
            segundos = segundos_por_contagem(horas, minutos)

        else:
            horario = entry_horario.get()
            segundos = segundos_ate_horario(horario)

    except ValueError:
        messagebox.showerror("Erro", "Valores inválidos.")
        return

    if segundos <= 0:
        messagebox.showerror("Erro", "Tempo deve ser maior que zero.")
        return

    executar_comando(acao, segundos)

    horario_final = datetime.now() + timedelta(seconds=segundos)
    messagebox.showinfo(
        "Sucesso",
        f"{acao.capitalize()} agendado para {horario_final.strftime('%H:%M:%S')}"
    )


def cancelar():
    cancelar_desligamento()
    messagebox.showinfo("Cancelado", "Ação cancelada com sucesso.")


# =========================
# JANELA
# =========================

janela = tk.Tk()
janela.title("Agendador de Desligamento / Reinício")
janela.geometry("380x320")
janela.resizable(False, False)

acao_var = tk.StringVar(value="desligar")
modo_var = tk.StringVar(value="contagem")

tk.Label(janela, text="Ação").pack()
tk.Radiobutton(janela, text="Desligar", variable=acao_var, value="desligar").pack()
tk.Radiobutton(janela, text="Reiniciar", variable=acao_var, value="reiniciar").pack()

tk.Label(janela, text="Modo").pack(pady=5)
tk.Radiobutton(janela, text="Contagem regressiva", variable=modo_var, value="contagem").pack()
tk.Radiobutton(janela, text="Horário específico (HH:MM)", variable=modo_var, value="horario").pack()

tk.Label(janela, text="Horas").pack()
entry_horas = tk.Entry(janela)
entry_horas.pack()

tk.Label(janela, text="Minutos").pack()
entry_minutos = tk.Entry(janela)
entry_minutos.pack()

tk.Label(janela, text="Horário (HH:MM)").pack(pady=5)
entry_horario = tk.Entry(janela)
entry_horario.pack()

tk.Button(janela, text="Executar", command=executar).pack(pady=8)
tk.Button(janela, text="Cancelar ação", command=cancelar).pack()

janela.mainloop()
