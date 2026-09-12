"""Step 2: chop the document into small, searchable chunks."""

from hr_assistant import config

from langchain_text_splitters import RecursiveCharacterTextSplitter

from hr_assistant.logger import get_logger

logger = get_logger(__name__)


def split_into_chunks(documents):
    """
    split document into small overlaping chunks.
    """
    text_splitter= RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP
    )
    chunks = text_splitter.split_documents(documents)
    logger.info("Split document(s) into %d chunk(s)", len(chunks))
    return chunks
   # return text_splitter.split_documents(documents)


