"""
Commands/Message handler.
Written by Daniil Ermolaev <blcklptn@icloud.com> 17.07.2023.
"""
from dispatcher import dp, bot
from . import texts

from aiogram import types
from aiogram.dispatcher import FSMContext
from . import buttons

@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.answer(texts.on_start, reply_markup=await buttons.generate_keyboard('index'))
