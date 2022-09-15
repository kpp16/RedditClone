from dotenv import load_dotenv, find_dotenv
import os

path = "D:\\Projects\\RedditClone\\backend\\app\\.env"

load_dotenv(dotenv_path=path)

DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_KEY = os.getenv("DATABASE_KEY")
DATABASE_NAME = os.getenv("DATABASE_NAME")

APP_NAME = os.environ.get("APP_NAME")