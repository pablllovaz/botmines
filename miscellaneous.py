import datetime
import random
from aiogram.utils.markdown import hcode, hbold, hitalic

def gerar_sinal():
  m = [
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1]
  ]
  w = 0
  while w < 3:
    y = random.randint(0,4)
    x = random.randint(0,4)
    if m[x][y] != 0:
      m[x][y] = 0
      w += 1

  hora = datetime.datetime.now().hour
  minuto = datetime.datetime.now().minute
  minuto += 1
  if minuto > 59:
    if hora == 23:
      hora = 0
    else:
      hora += 1
    minuto -=60
  hora = str(hora)
  minuto = str(minuto)
  if len(hora) == 1:
    hora = "0"+hora
  if len(minuto) == 1:
    minuto = "0"+minuto

  sinal = f"""💰 Entrada Confirmada 💰
🚨 N° de tentativas: {random.randint(2,5)}
💣 03 MINAS
🕑 Entrada: {hora}:{minuto}\n\n"""

  for i in range(5):
    for j in range(5):
      if m[i][j] == 0:
        slot = '⭐️'
      else:
        slot = '🟦'
      sinal += slot
    sinal += '\n'

  return sinal
