import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_URL = os.environ.get('DATABASE_URL', f'sqlite:///{BASE_DIR/"research.db"}')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

COST_PER_QUESTION = 1
COST_PER_REPORT = 2