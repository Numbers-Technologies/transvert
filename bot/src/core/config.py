# All settings data from .env will be in Settings class.
# Written by Daniil Ermolaev <blcklptn@icloud.com> 17.07.2023
from pydantic import BaseSettings
from dotenv import load_dotenv


load_dotenv()

class Settings(BaseSettings):
    BOT_TOKEN: str

settings = Settings()
