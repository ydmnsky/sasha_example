import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import pyparsing

# Enable logging
logging.basicConfig(level=logging.INFO)

# Set up bot and dispatcher
TOKEN = "6156298567:AAHMQL3aYwt1BrSimGQd91R2Uds7cAjzeQg"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#123
#123
#123
#123
#123
#123
#123
#123
#123
#123
#123
#123
#123
# Define the handler for the /start command
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("Привет! Отправь мне название песни и я пришлю тебе клип!")


# Define the handler for all other messages
@dp.message_handler()
async def echo_handler(message: types.Message):
    link = "Здесь будет ссылка на клип"
    # TODO
    await message.answer(link)


# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
