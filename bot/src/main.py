# Main function that run all bot.
# Written by Daniil Ermolaev <blcklptn@icloud.com> 17.07.2023.

from dispatcher import *
from frontend.handlers.message_handlers import *


if __name__ == '__main__':
    executor.start_polling(dp) # db ~ custom dispatcher implementation
