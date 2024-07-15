import os
import datetime
from tkinter import *

agora = datetime.datetime.now()

def relogio(hora_marcada):
    tempo = datetime.datetime.strptime(hora_marcada, '%H:%M').replace(year=agora.year, month=agora.month, day=agora.day)
    if tempo < agora:
        tempo = tempo + datetime.timedelta(days=1)
    hora_marcada = (tempo - agora).seconds
    os.system(f'shutdown /{escolha.get()} /t {hora_marcada}')

def cronometro(hora_marcada):
    tempo = datetime.datetime.strptime(hora_marcada, '%H:%M').replace(year=agora.year, month=agora.month, day=agora.day)
    if tempo < agora:
        tempo = tempo + datetime.timedelta(days=1)
    hora_marcada = (tempo - agora).seconds
    os.system(f'shutdown /{escolha.get()} /t {hora_marcada}')

def cancelar():
    os.system('shutdown /a')

root = Tk()

escolha = StringVar()
opcao = StringVar()
hora_marcada = StringVar()

Label(root, text="Escolha entre desligar (s) e reiniciar (r):").pack()
Radiobutton(root, text="Desligar", variable=escolha, value='s').pack()
Radiobutton(root, text="Reiniciar", variable=escolha, value='r').pack()

Label(root, text="Escolha entre definir horario (1) e contagem regressiva (2):").pack()
Radiobutton(root, text="Definir horario", variable=opcao, value='1').pack()
Radiobutton(root, text="Contagem regressiva", variable=opcao, value='2').pack()

Label(root, text="Digite a hora ou o tempo até desligar:").pack()
Entry(root, textvariable=hora_marcada).pack()

Button(root, text="Confirmar", command=lambda: relogio(hora_marcada.get()) if opcao.get() == '1' else cronometro(hora_marcada.get())).pack()
Button(root, text="Cancelar desligamento", command=cancelar).pack()

root.mainloop()

