import telebot
import requests
import time
from telebot import types
bot = telebot.TeleBot('5496942470:AAGpQimJH4Ox2GoKm4T5j0NhYxN8OVk6On8')
@bot.message_handler(regexp="ايدي")
def text(message):
	f2 = message.from_user.first_name 
	t2 = message.from_user.username
	id = message.from_user.id
	info = bot.get_chat(message.from_user.id)
	bio = info.bio
	b4 = types.InlineKeyboardMarkup()
	b = types.InlineKeyboardButton(f"𝙣𝙖𝙢𝙚 ✯ {f2}",f"https://t.me/{message.from_user.username}")
	b1 = types.InlineKeyboardButton(f"𝙪𝙨𝙚𝙧 ✯ @{t2}","https://t.me/{t2}")
	b3 = types.InlineKeyboardButton(f" 𝙞𝙙 ✯ {id}",url=f"https://t.me/{t2}")
	b5 = types.InlineKeyboardButton(f"𝙗𝙞𝙤 ✯ {bio}",url=f"https://t.me/{t2}")
	t = time.strftime("%p %H:%M")
	t1 = types.InlineKeyboardButton(f"𝙩𝙞𝙢𝙚 ✯ {t}",url=f"https://t.me/{t2}")
	b4.add(b1)
	b4.add(b)
	b4.add(b3)
	b4.add(t1)
	b4.add(b5)
	b11 = types.InlineKeyboardButton("جديدنا ",url="t.me/pjpppppp")
	b4.add(b11)
	url = f"https://t.me/{message.from_user.username}"
	bot.send_photo(message.chat.id,url,f"id [[?]] `{id}` ",parse_mode="markdown",reply_markup=b4,reply_to_message_id=message.message_id)	
bot.polling(True)	
