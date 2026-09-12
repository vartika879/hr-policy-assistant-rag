"""Step 4: store chunk embeddings in Qdrant Cloud so we can search them later."""

import os 
from langchain_community.vectorstores import FAISS

from hr_assistant import config

from hr_assistant.embeddings import get_embeddings_models
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

# biliding a vector store using Fiass

def build_vector_store(chunks):
    """Embed every chunk and build a searchable FAISS index in memory"""
    logger.info(
        "Embedding %d chunk(s) and uploading to database collection '%s'...",
        len(chunks),)
    embeddings_model=get_embeddings_models()
    
    return FAISS.from_documents(chunks,embeddings_model)

# save Vector Store

def save_vector_store(vector_store,path:str=config.VECTOR_STORE_PATH)->None:
    """ save the faiss index to disk so we dont have to rebuild it every time"""
    vector_store.save_local(path)

def load_vector_store(path:str=config.VECTOR_STORE_PATH):
    """Load a previously saved Faiss index from disk"""
    embeddings_models = get_embeddings_models()

    return FAISS.load_local(path,embeddings_models,allow_dangerous_deserialization=True)

def vector_store_exixts(path:str=config.VECTOR_STORE_PATH)->bool:
    """
    Check if a saved FAISS index already exists on disk
    """
    return os.path.exists(os.path.join(path,"index.faiss"))

def get_retriever(vector_store,k:int=config.TOP_K_RESULTS):
    """Turn a vector store into a retriever that return the top-k matching chunks"""
    return vector_store.as_retriever(search_kwargs={"k":k})
