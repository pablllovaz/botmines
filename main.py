import asyncio
import logging
import sys
import random

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.markdown import hcode, hbold, hitalic
from dbmanager import *
from miscellaneous import *

TOKEN = ("6555641047:AAGtRnjH6e3O5_1NAa6pDJT5zBPK0C4ke6g")

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
ADMIN_SUPREMO = '5915298829'

@dp.message(CommandStart())
async def inicializao(message: Message) -> None:
  await message.answer(f"OLÁ, {hbold(message.from_user.full_name)}! ❌VOCÊ NÃO POSSUI ACESSO!")

@dp.message(Command('alertageral'))
async def alerta(message: Message) -> None:
  await message.answer(f"""🎃𝗔𝗟𝗘𝗥𝗧𝗔𝗥 𝗚𝗘𝗥𝗔𝗟 - 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗥🎄
\n
Vᴏᴄᴇ̂ ᴇɴᴠɪᴀʀᴀ ᴜᴍᴀ ᴍᴇɴsᴀɢᴇᴍ ᴘᴀʀᴀ ᴛᴏᴅᴏs ᴏs ᴄᴀɴᴀɪs, Vᴏᴄᴇ̂ ᴘᴏᴅᴇ ᴇɴᴠɪᴀʀ ᴠɪᴅᴇᴏs, ɪᴍᴀɢᴇɴs ᴇ ᴛᴇxᴛᴏs! Usᴀɴᴅᴏ ᴏ ᴘʀᴇғɪxᴏ [ALERTAR] ɴᴀ ᴅᴇsᴄʀɪᴄ̧ᴀ̃ᴏ ᴅᴏ ᴠɪ́ᴅᴇᴏ ᴏᴜ ɪᴍᴀɢᴇᴍ!
\n
 ⚠️𝗩𝗲𝗷𝗮 𝗮𝗯𝗮𝗶𝘅𝗼 𝘂𝗺 𝗲𝘅𝗲𝗺𝗽𝗹𝗼 𝗱𝗲 𝗰𝗼𝗺𝗼 𝗻𝗼𝘁𝗶𝗳𝗶𝗰𝗮𝗿:
  
[ALERTA] BOA TARDE A TODOS!""")
  
  
  
@dp.message(Command('adicionar'))
async def addadmin(message: Message, command: CommandObject) -> None:
  quem_enviou_o_comando = str(message.from_user.id)
  if quem_enviou_o_comando == ADMIN_SUPREMO:
    if command.args not in get_admins():
      add_admin(command.args)
      await message.answer(f"ADMIN {command.args} ADICIONADO COM SUCESSO! ✅")
    else:
      await message.answer(f"ADMIM JÁ E ADMIN. ❌")
  else:
    await message.answer(f"VOCÊ NÃO TEM PERMISSÃO PARA ADICIONAR ADMINS!. ❌")

@dp.message(Command('listaradmins'))
async def listadmin(message: Message, command: CommandObject) -> None:
  quem_enviou_o_comando = str(message.from_user.id)
  if quem_enviou_o_comando == ADMIN_SUPREMO:
    if len(get_admins()) > 0:
      msg = "📌ESTES SÃO OS ADMINISTRADORES NO SISTEMA:\n\n"
      for adm in get_admins():
        msg += f"  ━━━━━━━━ ● ━━━━━━━━ \n🧑🏻QUEM ADICIONOU: VOCÊ \n🆔USER ID:{hcode(adm)}\n"
      await message.answer(msg)
    else:
      await message.answer(f"NO MOMENTO NÃO HÁ ADMINS CADASTRADOS! ❌")
  else:
    await message.answer(f"VOCÊ NÃO TEM PERMISSÃO PARA LISTAR ADMINS. ❌")

@dp.message(Command('remover'))
async def addadmin(message: Message, command: CommandObject) -> None:
  quem_enviou_o_comando = str(message.from_user.id)
  if quem_enviou_o_comando == ADMIN_SUPREMO:
    if command.args in get_admins():
      del_admin(command.args)
      await message.answer(f"ADMIN {command.args} REMOVIDO COM SUCESSO!✅")
    else:
      await message.answer(f"ADMINISTRADOR NÃO EXISTE ❌")
  else:
    await message.answer(f"VOCÊ NÃO TEM PERMISSÃO PARA REMOVER ADMINS! ❌")


@dp.message(Command('removercanal'))
async def delchannel(message: Message, command: CommandObject) -> None:
  quem_enviou_o_comando = str(message.from_user.id)
  if quem_enviou_o_comando in get_admins():
    if command.args in get_channels_cid():
      del_channel(command.args)
      await message.answer(f"CANAL {command.args} REMOVIDO COM SUCESSO! ✅")
    else:
      await message.answer(f"CANAL {command.args} NÃO ENCONTRADO! ❌")
  else:
    await message.answer(f"VOCÊ NÃO TEM PERMISSÃO PARA REMOVER ADMINS! ❌")

@dp.message(Command('listarcanais'))
async def listchannels(message: Message, command: CommandObject) -> None:
  quem_enviou_o_comando = str(message.from_user.id)
  if len(get_admins()) > 0:
    if quem_enviou_o_comando in get_admins():
      msg = "📌ESSES SÃO OS CANAIS PRESENTES:\n\n"
      for channel in get_channels():
          msg += f"  ━━━━━━━━ ● ━━━━━━━━ \n🧑🏻NOME DO CANAL: {channel['channel_name']}\n🆔CHAT ID: {hcode(channel['chat_id'])}\n🎃INDENTIFICADOR: {channel['author']}\n\n"
      await message.answer(msg)
    else:
      await message.answer(f"VOCÊ NÃO TEM PERMISSÃO PARA LISTAR CANAIS! ❌")
  else:
    await message.answer(f"SEM CANAIS CADASTRADOS! ❌")

@dp.message(Command('iniciar'))
async def sendsignal(message: Message) -> None:
  quem_enviou_o_comando = str(message.from_user.id)
  if quem_enviou_o_comando in get_admins():
    if len(get_channels()) > 0:
      await message.answer(f"O ENVIO PROGRAMADO FOI ATIVADO COM SUCESSO!✅")
      while True:
        for channel in get_channels():
          cid = channel['chat_id']
          txt = f"{gerar_sinal()}\n\n<a href='{channel['link']}'>🙈𝗔𝗕𝗥𝗜𝗥 - 𝗠𝗜𝗡𝗘𝗦 (𝗖𝗟𝗜𝗤𝗨𝗘 𝗔𝗤𝗨𝗜)💣</a> \n<a href='{channel['link']}'>🍀𝗖𝗔𝗗𝗔𝗦𝗧𝗥𝗔-𝗦𝗘 (𝗖𝗟𝗜𝗤𝗨𝗘 𝗔𝗤𝗨𝗜)🎃</a>"
          try:
            await bot.send_message(chat_id=cid, text=txt, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
          except:
            await message.answer(f"ERRO AO ENVIAR SINAL AO CANAL {cid}! ❌ \n ENTRE EM CONTATO COM O SUPORTE: @pabolovaz")
        espera = random.randint(1500, 2560)
        await asyncio.sleep(espera)
    else:
      await message.answer(f"SEM CANAIS CADASTRADOS PARA ENVIAR! ❌")
    
  else:
    await message.answer(f"OLÁ, {hbold(message.from_user.full_name)}! VOCÊ NÃO POSSUI ACESSO! ❌")

@dp.message(Command('id'))
async def myid(message: Message) -> None:
  await message.answer(f""" 🎃𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗖𝗢𝗘𝗦 𝗗𝗢 𝗚𝗥𝗨𝗣𝗢:
🌎𝗜𝗗 𝗖𝗛𝗔𝗧: {message.chat.id}

👻𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗖𝗢𝗘𝗦 𝗗𝗢 𝗨𝗦𝗨𝗔𝗥𝗜𝗢:
🆔𝗨𝗦𝗘𝗥 𝗜𝗗: {hcode(message.from_user.id)}
💁🏼𝗡𝗢𝗠𝗘: {message.from_user.full_name}
🙈𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘: @{message.from_user.username} """)

@dp.message(Command('ajuda'))
async def ajd(message: Message) -> None:
  await message.answer(f"""🥹AJUDA - PARA ADMINS🚀

⚠️ATENÇÃO: Avise ao contratante, Adicionar este bot ao canal! Conceder permissões administrativas ao bot!

1°.) VINCULAR BOT AO CANAL!👀

O bot já com as permissões necessárias, Utilize o comando:
    
=> /REGISTRAR [LINK DE AFILIADO] [INDETIFICADOR]

🤩EXEMPLO: /REGISTRAR blaze.com José

⚠️ATENÇÃO: E RECOMENDADO QUE O LINK FORNECIDO DE AFILIADO SEJA INCURTADO. Você pode utilizar:

https://bitly.com/
https://short.io/pt

⚠️ATENÇÃO: O INDENTIFICADOR DEVE SER CURTO.

🔴COMANDOS ADMIN SUPREMO:

/adicionar [USER ID]
    => ADICIONA ADMINS.

/remover [USER ID]
    => REMOVER ADMINS.

/listaradmins
    => LISTA DE ADMINS.

🟢COMANDOS ADMINISTRADORES:

/iniciar
    => INICIAR ENVIO DE SINAIS PG.

/listarcanais
   => LISTA DE CANAIS PRESENTES.

/removercanal [CHAT ID]
   => REMOVER CANAIS.

/alertageral
   => NOTIFICA TODOS CANAIS.

/id
   => INFORMAÇÕES DO USUÁRIO.

🚀CASO TENHA ALGUMA DÚVIDA ENTRE EM CONTATO COM O SUPORTE: @pabolovaz 🍀""")

@dp.callback_query()
async def random_value(call: types.CallbackQuery):
    if "permitir" in call.data:
        cid = call.data.split(" ")[1]
        link = call.data.split(" ")[2]
        channel_name = "'"+call.data.split("'")[1]+"'"
        author = call.data.split(" ")[-1]
        add_channel(cid, link, channel_name, author)
        for admin_id in get_admins():
          await call.message.delete()
          await bot.send_message(chat_id=admin_id, text=f"""CANAL {channel_name} AUTORIZADO! ✅ \n Utilize o comamdo /listarcanais para mais informaões""")
    if call.data == "recusar":
        await call.message.delete()

@dp.channel_post(Command('registrar'))
async def channel_post_handler(channel_post: types.Message, command: CommandObject) -> None:
  cid = str(channel_post.chat.id)
  if cid not in get_channels_cid():
    link = command.args.split(" ")[0]
    author = command.args.split(" ")[1]
    channel_name = channel_post.chat.title[:9]+"..."
    button1 = InlineKeyboardButton(text="Permitir", callback_data=f"permitir {cid} {link} '{channel_name}' {author}")
    button2 = InlineKeyboardButton(text="Recusar", callback_data=f"recusar")
    keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[[button1, button2]])

  
    txt = f"🌚UMA NOVA SOLICITAÇÃO DE REGISTRO! \n  \n 🔥CANAL: \"{channel_name}\" \n 👑INDENTIFICADOR: {author} , \n ❗️ID DO CANAL: {cid} \n 💎LINK DE AFILIADO: {link}"
    for admin_id in get_admins():
      await bot.send_message(chat_id=admin_id, text=txt, reply_markup=keyboard_inline)

@dp.message()
async def alertageral(message: types.Message) -> None: 
  if len(get_channels()) > 0:
    if str(message.from_user.id) in get_admins():
      try:
        text = message.caption[:8]
      except:
        text = message.text[:8]
      if text[:8] == '[alerta]':
        print("to aqui")
        for channel in get_channels_cid():
          await bot.copy_message(chat_id=channel, from_chat_id=message.chat.id, message_id=message.message_id)
    else:
      await message.answer(f"VOCÊ NÂO TEM PERMISSÃO PARA ALERTAR CANAIS. \n \n Caso tente novamente sua conta do telegram será bloqueada! ❌")
  else:
    await message.answer(f"Sem canais no sistema! ❌")

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
