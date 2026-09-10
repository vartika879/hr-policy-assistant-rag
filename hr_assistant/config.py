import os 
from dotenv import load_dotenv

load_dotenv()


## ENV VAR/ SECRET
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
COHERE_API_KEY=os.getenv("COHERE_API_KEY")



## DEFINE THE PATH-- DATA / VECTOR STORE
DATA_FILE_PATH=os.path.join("Data","hr_policy.txt")

VECTOR_STORE_PATH=os.path.join("Data","faiss_index")



## MODELS

# LLM AND EMBEDDING MODEL

LLM_MODEL_NAME = "openai/gpt-oss-20b"

EMBEDDING_MODEL = "embed-english-light-v3.0"

# CHUNK AND TEXT SPLITTING CONFIG

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# RETRIEVAL RESULTS

TOP_K_RESULTS = 3 

# SYSTEM INSTRUCTIONS

SYSTEM_PROMPT = ("you are afriendly HR assistant working for acme crop." \
    "Always use the search_hr_policy tool to look up " \
    "fact before answering . if the answer isn't in the search result, say you dont know instead of guessing ."
    
)

def check_api_key()->None:
    """Stop early with a clear mesage if a required API key is missing """
    if not GROQ_API_KEY:
        raise ValueError("Groq api is missing")
    if not COHERE_API_KEY:
            raise ValueError("Groq api is missing")
    