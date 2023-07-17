# All settings data from .env will be in Settings class.
# Written by Daniil Ermolaev <blcklptn@icloud.com> 17.07.2023

from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()

class Settings(BaseSettings):
    TOKEN: str

settings = Settings()
