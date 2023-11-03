import sqlite3

conn = sqlite3.connect('bot.db')
conn.execute("CREATE TABLE IF NOT EXISTS admins (chat_id TEXT);")
conn.execute("CREATE TABLE IF NOT EXISTS channels (chat_id TEXT, link TEXT, channel_name TEXT, author TEXT);")
conn.commit()
conn.close()

def add_admin(chat_id):
  conn = sqlite3.connect('bot.db')
  conn.execute(f"INSERT INTO admins (chat_id) VALUES ({chat_id});")
  conn.commit()
  conn.close()

def del_admin(chat_id):
  conn = sqlite3.connect('bot.db')
  conn.execute(f"DELETE FROM admins WHERE chat_id == {chat_id};")
  conn.commit()
  conn.close()

def get_admins():
  admins = []
  conn = sqlite3.connect('bot.db')
  cursor = conn.execute("SELECT * FROM admins;")
  for row in cursor:
    admins.append(row[0])
  conn.close()
  return admins
  
def add_channel(chat_id, link, channel_name, author):
  channel_name = channel_name[1:-1]
  conn = sqlite3.connect('bot.db')
  conn.execute(f"INSERT INTO channels (chat_id, link, channel_name, author) VALUES ('{chat_id}', '{link}', '{channel_name}', '{author}');")
  conn.commit()
  conn.close()

def del_channel(chat_id):
  conn = sqlite3.connect('bot.db')
  conn.execute(f"DELETE FROM channels WHERE chat_id == '{chat_id}';")
  conn.commit()
  conn.close()

def get_channels():
  channels = []
  conn = sqlite3.connect('bot.db')
  cursor = conn.execute("SELECT * FROM channels;")
  for row in cursor:
      channels.append({'chat_id': row[0], 'link': row[1], 'channel_name': row[2], 'author': row[3]})
  conn.close()
  return channels
  
def get_channels_cid():
  channels = []
  conn = sqlite3.connect('bot.db')
  cursor = conn.execute("SELECT * FROM channels;")
  for row in cursor:
    channels.append(row[0])
  conn.close()
  return channels
  
