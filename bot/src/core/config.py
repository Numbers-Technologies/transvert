# All settings data from .env will be in Settings class.
# Written by Daniil Ermolaev <blcklptn@icloud.com> 17.07.2023
from pydantic import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str

settings = Settings()
