import os
import datetime
agora = datetime.datetime.now()
semana = agora.weekday()
hora = agora.hour
if 0 == semana <= 3 or semana == 6:
    x = '22:00'
    tempo = datetime.datetime.strptime(x, '%H:%M').replace(year=agora.year, month=agora.month, day=agora.day)
    hora_desligar = (tempo - agora).seconds
    os.system(f'shutdown /s /t {hora_desligar}')
