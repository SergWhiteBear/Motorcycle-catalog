from dotenv import load_dotenv
import os

from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    DB_HOST: str = os.environ.get("DB_HOST")
    DB_PORT: int = os.environ.get("DB_PORT")
    DB_NAME: str = os.environ.get("DB_NAME")
    DB_USER: str = os.environ.get("DB_USER")
    DB_PASSWORD: str = os.environ.get("DB_PASSWORD")
    DB_URL: str = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SMTP_PASSWORD: str = os.environ.get("SMTP_PASSWORD")
    SMTP_HOST: str = os.environ.get("SMTP_HOST")
    BOT_TOKEN: str = os.environ.get("BOT_TOKEN")
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    ALGORITHM: str = os.environ.get("ALGORITHM")

    class Config:
        env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")


settings = Settings()

database_url = settings.DB_URL
