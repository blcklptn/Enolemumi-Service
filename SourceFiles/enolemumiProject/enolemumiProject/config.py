from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Config(BaseSettings):
    DB_USERNAME: str
    DB_PORT: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_NAME: str

config = Config()