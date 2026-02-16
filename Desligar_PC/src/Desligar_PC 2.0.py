import os
import platform
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox, ttk

# =========================
# LÓGICA DE SISTEMA
# =========================

def sistema_suportado():
    return platform.system() == "Windows"

def executar_comando(acao: str, segundos: int):
    acao_cmd = acao.lower()
    if acao_cmd == "desligar":
        os.system(f"shutdown /s /t {segundos}")
    elif acao_cmd == "reiniciar":
        os.system(f"shutdown /r /t {segundos}")

def cancelar():
    os.system("shutdown /a")
    messagebox.showinfo("Cancelado", "Agendamento cancelado com sucesso!")

# =========================
# LÓGICA DE INTERFACE DINÂMICA
# =========================

def atualizar_interface(*args):
    modo = modo_var.get()
    if modo == "Contagem":
        frame_horario_especifico.pack_forget()
        frame_contagem.pack(pady=2)
    else:
        frame_contagem.pack_forget()
        frame_horario_especifico.pack(pady=2)
    
    # Ajusta para uma altura bem pequena e justa
    janela.geometry("320x140") 

# =========================
# INTERFACE PRINCIPAL
# =========================

janela = tk.Tk()
janela.title("Power Manager")
janela.geometry("320x140")
janela.resizable(False, False)

# --- Frame Topo (Ação e Modo) ---
frame_top = tk.Frame(janela)
frame_top.pack(pady=10)

tk.Label(frame_top, text="Ação:").grid(row=0, column=0, padx=2)
acao_var = tk.StringVar(value="Desligar")
ttk.OptionMenu(frame_top, acao_var, "Desligar", "Desligar", "Reiniciar").grid(row=0, column=1)

tk.Label(frame_top, text=" Modo:").grid(row=0, column=2, padx=2)
modo_var = tk.StringVar(value="Contagem")
modo_var.trace("w", atualizar_interface) # Apenas um trace é necessário
ttk.OptionMenu(frame_top, modo_var, "Contagem", "Contagem", "Horário").grid(row=0, column=3)

# --- Container para Contagem Regressiva ---
frame_contagem = tk.Frame(janela)

# Label "Horas" na coluna 0, Entry na coluna 1
tk.Label(frame_contagem, text="Horas:").grid(row=0, column=0, padx=2)
entry_horas = tk.Entry(frame_contagem, width=5)
entry_horas.grid(row=0, column=1, padx=5)

# Label "Minutos" na coluna 2, Entry na coluna 3
tk.Label(frame_contagem, text="Minutos:").grid(row=0, column=2, padx=2)
entry_minutos = tk.Entry(frame_contagem, width=5)
entry_minutos.grid(row=0, column=3, padx=5)

# --- Container para Horário Específico ---
frame_horario_especifico = tk.Frame(janela)
tk.Label(frame_horario_especifico, text="Horário (HH:MM):").grid(row=0, column=0)
entry_horario = tk.Entry(frame_horario_especifico, width=10)
entry_horario.grid(row=0, column=1, padx=5)

# --- Botões (Removido side=BOTTOM para colar nos campos) ---
frame_btns = tk.Frame(janela)
frame_btns.pack(pady=10) 

def preparar_execucao():
    try:
        if modo_var.get() == "Contagem":
            h = int(entry_horas.get() or 0)
            m = int(entry_minutos.get() or 0)
            segundos = h * 3600 + m * 60
        else:
            agora = datetime.now()
            alvo = datetime.strptime(entry_horario.get(), "%H:%M").replace(
                year=agora.year, month=agora.month, day=agora.day)
            if alvo <= agora: alvo += timedelta(days=1)
            segundos = int((alvo - agora).total_seconds())
        
        if segundos <= 0: raise ValueError
        executar_comando(acao_var.get(), segundos)
        messagebox.showinfo("Sucesso", "Agendado!")
    except:
        messagebox.showerror("Erro", "Formato inválido!")

btn_exec = tk.Button(frame_btns, text="Executar", command=preparar_execucao, width=10, bg="#d1ffd1")
btn_exec.pack(side=tk.LEFT, padx=5)

btn_canc = tk.Button(frame_btns, text="Cancelar", command=cancelar, width=10, fg="red")
btn_canc.pack(side=tk.LEFT, padx=5)

# Inicializa
atualizar_interface()
janela.mainloop()