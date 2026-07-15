from dotenv import load_dotenv
import os

load_dotenv()

SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

USE_WINDOWS_AUTH = os.getenv(
    "USE_WINDOWS_AUTH",
    "True"
).lower() == "true"