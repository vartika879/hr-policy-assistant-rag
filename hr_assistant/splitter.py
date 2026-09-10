from hr_assistant import config

from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_into_chunks(documents):
    """
    split document into small overlaping chunks.
    """
    text_splitter= RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP
    )
    return text_splitter.split_documents(documents)


