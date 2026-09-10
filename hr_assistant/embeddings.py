from langchain_cohere import CohereEmbeddings
from hr_assistant import config

def get_embeddings_models():
    """
    Return a Cohere Embeddings model . Read COHERE_API_KEY from the environment.
    """
    return CohereEmbeddings(model=config.EMBEDDING_MODEL)

