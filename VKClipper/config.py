# Getting env variables using os module
# Written by Daniil Ermolaev <blcklptn@icloud.com> 18.07.2023

import os

VK_TOKEN = os.getenv('VK_TOKEN')
REFRESH_RATE = int(os.getenv('REFRESH_RATE'))
GROUP_NAME = os.getenv('GROUP_NAME')
