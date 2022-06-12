from config import*
import ha
from aiogram import Bot
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher


bot = Bot(Telegram_bot_token)
dp = Dispatcher(bot)
@dp.message_handler(content_types=['text'])
async def get_text_messages(message):
	if message.text.startswith("/token"):
		token=message.text.split(" ")
		if len (token)<=1:
			await bot.send_message(message.from_user.id, "Напиши коректный токен \nПример:\n \n/token vk1.a.DBfDMF5rtPQqrkYubD_sBGUPAAxR2FgcBgSpwjEizbYarbMpOi-fWMl4DLoedllqUNgpHo8EK-Oidfm8Hl7NnDnMhL4YUnPIGMuW8ZyGw3WYadwQdqg0ZtTT1RTC4AIBd7kT_kyaTDCAps_QEiLVy4_mT1dOOVaWmQBR3mOQhJU5d5M1AMZPqwj8Z9KxE4VH\n", "html")
			return


		try:
			worker=ha.worker(token[1])
		except:
			await bot.send_message(message.from_user.id, "Напиши коректный токен \nПример:\n \n/token vk1.a.DBfDMF5rtPQqrkYubD_sBGUPAAxR2FgcBgSpwjEizbYarbMpOi-fWMl4DLoedllqUNgpHo8EK-Oidfm8Hl7NnDnMhL4YUnPIGMuW8ZyGw3WYadwQdqg0ZtTT1RTC4AIBd7kT_kyaTDCAps_QEiLVy4_mT1dOOVaWmQBR3mOQhJU5d5M1AMZPqwj8Z9KxE4VH\n", "html")
			return


		try: 
			worker.add_friends()
		except:
			await bot.send_message(message.from_user.id, "Ошибка❌")
			return


		try:
			worker.add_likes()
		except:
			await bot.send_message(message.from_user.id, "Ошибка при оставлении лайка❌")


		try:
			worker.add_photo()
		except:
			await bot.send_message(message.from_user.id, "Ошибка при ретвите❌")


		try:
			worker.add_gift()
		except:
			await bot.send_message(message.from_user.id, "Ошибка при отправке подарка❌")


		await message.answer("Работа завершена✅")
	elif message.text == "/help":
		await bot.send_message(message.from_user.id, "Напиши <code>/token</code>", "html")
	else:
		await bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

