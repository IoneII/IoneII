from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token='хх')
dp = Dispatcher(bot)

@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = 'Станислав выбирает, что же сюда прислать, а пока посмотрите фотки.'
    await bot.send_message(chat_id=chat_id, text=text)
    #sent_message = await bot.send_message(chat_id=chat_id, text=text)
    #print(sent_message.to_python())
    sent_message = await bot.send_photo(chat_id=chat_id, photo='https://vk.com/kiberone.anapa?z=photo-206628619_457240064%2Falbum-206628619_00%2Frev')
executor.start_polling(dp)

