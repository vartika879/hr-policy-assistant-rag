"""Step 4: store chunk embeddings in Qdrant Cloud so we can search them later."""

import os 
from langchain_community.vectorstores import FAISS

from hr_assistant import config

from hr_assistant.embeddings import get_embeddings_models
from hr_assistant.logger import get_logger


from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient


logger = get_logger(__name__)

# biliding a vector store using Fiass

def build_vector_store(chunks):
    """Embed every chunk upload it into a qdrant cloud collection"""
    logger.info(
        "Embedding %d chunk(s) and uploading to qdrant collection '%s'...",
        len(chunks),
        config.QDRANT_COLLECTION_NAME)
    embeddings_model=get_embeddings_models()
    
    vector_store = QdrantVectorStore.from_documents(
        chunks,
        embedding=embeddings_model,
        url=config.QDRANT_URL,
        api_key= config.QDRANT_API_KEY,
        collection_name=config.QDRANT_COLLECTION_NAME
    )
    logger.info("Uploaded to qdrant collection '%s'",config.QDRANT_COLLECTION_NAME)
    return vector_store
# save Vector Store
"""
def save_vector_store(vector_store,path:str=config.VECTOR_STORE_PATH)->None:
     save the faiss index to disk so we dont have to rebuild it every time
    vector_store.save_local(path)
"""


def load_vector_store():
    """ Connnect to Qdrant cloud collection that was already built before"""
    logger.info("Connecting to the quadrant clloud")
    embeddings_models = get_embeddings_models()

    return QdrantVectorStore.from_documents(
        embeddings=embeddings_model,
        url=config.QDRANT_URL,
        api_key= config.QDRANT_API_KEY,
        collection_name=config.QDRANT_COLLECTION_NAME
    )








def vector_store_exixts()->bool:
    """
    Check if qdrant store already exists
    """
    client=QdrantClient(
        url=config.QDRANT_URL,
        api_key=config.QDRANT_API_KEY,

    )
    return client.collection_exists(config.QDRANT_COLLECTION_NAME)



def get_retriever(vector_store,k:int=config.TOP_K_RESULTS):
    """Turn a vector store into a retriever that return the top-k matching chunks"""
    return vector_store.as_retriever(search_kwargs={"k":k})
