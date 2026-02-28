import os
import datetime
from tkinter import *

def get_current_time():
    return datetime.datetime.now()

def dezdanoite():
    os.system('shutdown /a')
    agora = datetime.datetime.now()
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
        print("Formato inválido. Use HH:MM")
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

root = Tk()
root.title("Agendador de Desligamento")

escolha = StringVar(value="Desligar")
opcao = StringVar(value="Definir horário")
hora_marcada = StringVar()

# Frame Ação
frame_acao = Frame(root)
frame_acao.pack(pady=5)

Label(frame_acao, text="Ação:").pack(side=LEFT, padx=5)
OptionMenu(frame_acao, escolha, "Desligar", "Reiniciar").pack(side=LEFT)

# Frame Tipo
frame_tipo = Frame(root)
frame_tipo.pack(pady=5)

Label(frame_tipo, text="Modo:").pack(side=LEFT, padx=5)
OptionMenu(frame_tipo, opcao, "Definir horário", "Contagem regressiva").pack(side=LEFT)

# Frame Entrada
frame_entrada = Frame(root)
frame_entrada.pack(pady=5)

Label(frame_entrada, text="Hora (HH:MM):").pack(side=LEFT, padx=5)
Entry(frame_entrada, textvariable=hora_marcada, width=10).pack(side=LEFT)

# Frame Botões
frame_botoes = Frame(root)
frame_botoes.pack(pady=10)

Button(frame_botoes, text="Confirmar",
       command=lambda: schedule_shutdown_or_restart(
           hora_marcada.get(), opcao.get(), escolha.get())
       ).pack(side=LEFT, padx=5)

Button(frame_botoes, text="Cancelar desligamento",
       command=cancelar).pack(side=LEFT, padx=5)

root.mainloop()