import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATA_UPLOADS_PATH = os.path.join(os.path.dirname(__file__), '../data/uploads')
VECTOR_DB_PATH = os.path.join(os.path.dirname(__file__), '../data/vector_dbs')
MAX_CHAT_MEMORY = 10

# Add other constants/configs as needed
