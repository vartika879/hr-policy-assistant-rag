"""All settings for the app live here, in one place."""

import os 
from dotenv import load_dotenv

load_dotenv()

def get_secret(key_name, default_value=None):
    """
    Safely fetch secrets for both Streamlit Cloud (st.secrets) 
    and Local CLI/VS Code (os.getenv).
    """
    try:
        import streamlit as st
        # Agar hum Streamlit environment me hain aur key secrets me exist karti hai
        if key_name in st.secrets:
            return st.secrets[key_name]
    except Exception:
        pass # Streamlit context ke bahar hone par error ignore karega
    
    # Agar cloud secrets me nahi mila, toh local .env se le lo
    return os.getenv(key_name, default_value)


## ENV VAR/ SECRET
GROQ_API_KEY = get_secret("GROQ_API_KEY")
COHERE_API_KEY = get_secret("COHERE_API_KEY")
GEMINI_API_KEY = get_secret("GEMINI_API_KEY")

# GATEWAY
PORTKEY_API_KEY = get_secret("PORTKEY_API_KEY")

GUARD_MODEL_NAME = "openai/gpt-oss-safeguard-20b"

#tracing
LANGSMITH_TRACING = get_secret("LANGSMITH_TRACING", "false")
LANGSMITH_ENDPOINT = get_secret("LANGSMITH_ENDPOINT")
LANGSMITH_API_KEY = get_secret("LANGSMITH_API_KEY")
LANGSMITH_PROJECT = get_secret("LANGSMITH_PROJECT")

## DEFINE THE PATH-- DATA / VECTOR STORE
DATA_FILE_PATH=os.path.join("Data","hr_policy.txt")


# VECTOR
QDRANT_URL= get_secret("QDRANT_URL")
QDRANT_API_KEY = get_secret("QDRANT_API_KEY")

QDRANT_COLLECTION_NAME = get_secret("QDRANT_COLLECTION_NAME","HR_policy")

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

def check_api_key() -> None:
    """Check required API keys and services."""
    if not PORTKEY_API_KEY:
        raise ValueError("PORTKEY_API_KEY is missing. Check .env or Streamlit Secrets.")

    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is missing. Check .env or Streamlit Secrets.")

    if not COHERE_API_KEY:
        raise ValueError("COHERE_API_KEY is missing. Check .env or Streamlit Secrets.")

    if not QDRANT_URL:
        raise ValueError("QDRANT_URL is missing. Check .env or Streamlit Secrets.")

    if not QDRANT_API_KEY:
        raise ValueError("QDRANT_API_KEY is missing. Check .env or Streamlit Secrets.")