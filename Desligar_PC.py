import os
import datetime
from tkinter import *

def get_current_time():
    return datetime.datetime.now()

def schedule_shutdown_or_restart(hora_marcada, opcao, escolha):
    agora = get_current_time()
    try:
        if opcao == '1':  # Definir horário
            tempo = datetime.datetime.strptime(hora_marcada, '%H:%M').replace(year=agora.year, month=agora.month, day=agora.day)
            if tempo < agora:
                tempo += datetime.timedelta(days=1)
            segundos_ate_hora_marcada = int((tempo - agora).total_seconds())
        elif opcao == '2':  # Contagem regressiva
            horas, minutos = map(int, hora_marcada.split(':'))
            segundos_ate_hora_marcada = horas * 3600 + minutos * 60
        else:
            print("Opção inválida.")
            return
    except ValueError:
        print("Formato de hora inválido. Use HH:MM.")
        return

    if escolha == 's':
        comando = 'shutdown /s /t'
    elif escolha == 'r':
        comando = 'shutdown /r /t'
    else:
        print("Escolha inválida para a ação.")
        return

    os.system(f'{comando} {segundos_ate_hora_marcada}')

def cancelar():
    os.system('shutdown /a')

root = Tk()

escolha = StringVar()
opcao = StringVar()
hora_marcada = StringVar()

Label(root, text="Escolha entre desligar (s) e reiniciar (r):").pack()
Radiobutton(root, text="Desligar", variable=escolha, value='s').pack()
Radiobutton(root, text="Reiniciar", variable=escolha, value='r').pack()

Label(root, text="Escolha entre definir horário (1) e contagem regressiva (2):").pack()
Radiobutton(root, text="Definir horário", variable=opcao, value='1').pack()
Radiobutton(root, text="Contagem regressiva", variable=opcao, value='2').pack()

Label(root, text="Digite a hora ou o tempo até desligar (HH:MM):").pack()
Entry(root, textvariable=hora_marcada).pack()

Button(root, text="Confirmar", command=lambda: schedule_shutdown_or_restart(hora_marcada.get(), opcao.get(), escolha.get())).pack()
Button(root, text="Cancelar desligamento", command=cancelar).pack()

root.mainloop()
