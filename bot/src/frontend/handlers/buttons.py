# Buttons generator for all pages.
#
# Example:
#    ```
#    reply_markup = await generate_keyboard('index')
#                        or
#    await generate_keyboard('upload_post')
#    ```

# Anyway generate_keyboard function will return rkm or ikm object with buttons.
# Written by Daniil Ermolaev <blcklptn@icloud.com> 17.07.2023.


from aiogram.types import ReplyKeyboardMarkup as rkm
from aiogram.types import InlineKeyboardMarkup as ikm

from aiogram.types import KeyboardButton as kb
from aiogram.types import InlineKeyboardButton as ikb


async def index_page() -> rkm:
    return rkm(resize_keyboard=True).add(kb('Выложить пост')).add(kb('Статус поста'))

async def generate_keyboard(for_page: str = 'index') -> rkm:
    if for_page == 'index': return await index_page()
