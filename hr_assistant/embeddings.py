"""Step 3: turn text into numbers (vectors) using Jina."""

from langchain_cohere import CohereEmbeddings
from hr_assistant import config

from hr_assistant.logger import get_logger

logger = get_logger(__name__)


def get_embeddings_models():
    """
    Return a Cohere Embeddings model . Read COHERE_API_KEY from the environment.
    """
    logger.info("Initializing embeddings model '%s'", config.EMBEDDING_MODEL)
    return CohereEmbeddings(model=config.EMBEDDING_MODEL)

