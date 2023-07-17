from aiogram.types import ReplyKeyboardMarkup as rkm
from aiogram.types import InlineKeyboardMarkup as ikm

from aiogram.types import KeyboardButton as kb
from aiogram.types import InlineKeyboardButton as ikb

async def index_page() -> rkm:
    return rkm(resize_keyboard=True).add(kb('Выложить пост')).add(kb('Статус поста'))

async def generate_keyboard(for_page: str = 'index') -> rkm:
    if for_page == 'index': return await index_page()
