import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Validate API key
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please add it to your .env file.")

DATA_UPLOADS_PATH = os.path.join(os.path.dirname(__file__), '../data/uploads')
VECTOR_DB_PATH = os.path.join(os.path.dirname(__file__), '../data/vector_dbs')
MAX_CHAT_MEMORY = 10

# Create necessary directories
os.makedirs(DATA_UPLOADS_PATH, exist_ok=True)
os.makedirs(VECTOR_DB_PATH, exist_ok=True)

# Add other constants/configs as needed
