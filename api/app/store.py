import os
from enum import Enum 
from dotenv import load_dotenv
load_dotenv()
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "WASP"
    dataDir: str = os.getcwd() + os.getenv('YAMLDB_BASEPATH')

class Tags(Enum):
    functions = "functions"
    langs = "langs"

settings = Settings()
tags = Tags