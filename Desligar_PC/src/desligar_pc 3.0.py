import os
import datetime
from tkinter import *
from tkinter import ttk, messagebox

# ============================
# FUNÇÕES DA ABA 1 (ORIGINAIS)
# ============================

def get_current_time():
    return datetime.datetime.now()

def dezdanoite():
    os.system('shutdown /a')
    agora = datetime.datetime.now()
    hora_desligar = datetime.time(22, 0)
    momento_desligar = datetime.datetime.combine(agora.date(), hora_desligar)

    if momento_desligar < agora:
        momento_desligar += datetime.timedelta(days=1)

    diferenca_tempo = int((momento_desligar - agora).total_seconds())
    os.system(f'shutdown /s /t {diferenca_tempo}')

def schedule_shutdown_or_restart(hora_marcada, opcao, escolha):
    agora = get_current_time()

    try:
        if opcao == 'Definir horário':
            tempo = datetime.datetime.strptime(hora_marcada, '%H:%M')
            tempo = tempo.replace(year=agora.year, month=agora.month, day=agora.day)

            if tempo < agora:
                tempo += datetime.timedelta(days=1)

            segundos = int((tempo - agora).total_seconds())

        elif opcao == 'Contagem regressiva':
            horas, minutos = map(int, hora_marcada.split(':'))
            segundos = horas * 3600 + minutos * 60
        else:
            return

    except ValueError:
        messagebox.showerror("Erro", "Formato inválido. Use HH:MM")
        return

    if escolha == 'Desligar':
        comando = 'shutdown /s /t'
    elif escolha == 'Reiniciar':
        comando = 'shutdown /r /t'
    else:
        return

    os.system(f'{comando} {segundos}')

def cancelar():
    os.system('shutdown /a')

# ============================
# FUNÇÕES DA ABA 2 (AUTOMÁTICO)
# ============================

def caminho_startup():
    return os.path.join(
        os.getenv('APPDATA'),
        r"Microsoft\Windows\Start Menu\Programs\Startup"
    )

def criar_automatico(hora, minuto):
    script_path = os.path.join(caminho_startup(), "desligar_auto_trabalho.py")

    conteudo = f"""
import os
from datetime import datetime, time, timedelta

agora = datetime.now()
dia = agora.weekday()

# Domingo(6) até Quinta(3)
if dia in [6,0,1,2,3]:

    horario = datetime.combine(agora.date(), time({hora}, {minuto}))

    if horario <= agora:
        horario += timedelta(days=1)

    segundos = int((horario - agora).total_seconds())

    os.system("shutdown /a")
    os.system(f"shutdown /s /t {{segundos}}")
"""

    with open(script_path, "w", encoding="utf-8") as f:
        f.write(conteudo)

    messagebox.showinfo("Ativado",
                        f"Automático definido para {hora:02d}:{minuto:02d}")

def remover_automatico():
    script_path = os.path.join(caminho_startup(), "desligar_auto_trabalho.py")

    if os.path.exists(script_path):
        os.remove(script_path)
        messagebox.showinfo("Removido", "Automático desativado.")
    else:
        messagebox.showinfo("Info", "Nenhum automático ativo.")

# ============================
# INTERFACE PRINCIPAL
# ============================

root = Tk()
root.title("Desligar PC 3.0")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# ============================
# ABA 1 (SEU CÓDIGO ORIGINAL)
# ============================

aba1 = Frame(notebook)
notebook.add(aba1, text="Manual")

escolha = StringVar(value="Desligar")
opcao = StringVar(value="Definir horário")
hora_marcada = StringVar()

frame_acao = Frame(aba1)
frame_acao.pack(pady=5)

Label(frame_acao, text="Ação:").pack(side=LEFT, padx=5)
OptionMenu(frame_acao, escolha, "Desligar", "Reiniciar").pack(side=LEFT)

frame_tipo = Frame(aba1)
frame_tipo.pack(pady=5)

Label(frame_tipo, text="Modo:").pack(side=LEFT, padx=5)
OptionMenu(frame_tipo, opcao, "Definir horário", "Contagem regressiva").pack(side=LEFT)

frame_entrada = Frame(aba1)
frame_entrada.pack(pady=5)

Label(frame_entrada, text="Hora (HH:MM):").pack(side=LEFT, padx=5)
Entry(frame_entrada, textvariable=hora_marcada, width=10).pack(side=LEFT)

frame_botoes = Frame(aba1)
frame_botoes.pack(pady=10)

Button(frame_botoes, text="Confirmar",
       command=lambda: schedule_shutdown_or_restart(
           hora_marcada.get(), opcao.get(), escolha.get())
       ).pack(side=LEFT, padx=5)

Button(frame_botoes, text="Cancelar desligamento",
       command=cancelar).pack(side=LEFT, padx=5)

Button(aba1, text="Desligar às 22:00",
       command=dezdanoite).pack(pady=5)

# ============================
# ABA 2 (AUTOMÁTICO)
# ============================

aba2 = Frame(notebook)
notebook.add(aba2, text="Automático")

Label(aba2, text="Horário fixo (HH:MM):").pack(pady=10)

entrada_auto = Entry(aba2, width=10)
entrada_auto.pack()

def ativar_auto():
    try:
        h, m = map(int, entrada_auto.get().split(":"))
        criar_automatico(h, m)
    except:
        messagebox.showerror("Erro", "Formato inválido. Use HH:MM")

frame_auto = Frame(aba2)
frame_auto.pack(pady=10)

Button(frame_auto, text="Ativar automático",
       command=ativar_auto).pack(side=LEFT, padx=5)

Button(frame_auto, text="Desativar automático",
       command=remover_automatico).pack(side=LEFT, padx=5)

root.mainloop()