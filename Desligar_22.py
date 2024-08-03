import os
import datetime

agora = datetime.datetime.now()
semana = agora.weekday()
hora = agora.hour

# Verifica se é domingo (0) a quinta-feira(4)
if 0 <= semana <= 4:
    x = '22:00'
    tempo = datetime.datetime.strptime(x, '%H:%M').replace(year=agora.year, month=agora.month, day=agora.day)
    # Se a hora de desligamento já passou, adicionar um dia
    if tempo < agora:
        tempo += datetime.timedelta(days=1)
        hora_desligar = (tempo - agora).seconds
        os.system(f'shutdown /s /t {hora_desligar}')
