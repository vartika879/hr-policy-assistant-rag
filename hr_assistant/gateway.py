"""step 6b Route the LLM through the Portkey gateway."""

from langchain_openai import ChatOpenAI
from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL

from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

GATEWAY_CONFIG_SLUG = "pc-hr-pol-d3a682"


def get_gateway_llm() -> ChatOpenAI:
    """Return the LLM routed through Portkey."""

    if not config.PORTKEY_API_KEY:
        raise ValueError("PORTKEY_API_KEY is missing")

    logger.info("Initializing Portkey gateway")
    logger.info("Portkey gateway URL: %s", PORTKEY_GATEWAY_URL)
    logger.info("Portkey config: %s", GATEWAY_CONFIG_SLUG)

    portkey_headers = createHeaders(
        api_key=config.PORTKEY_API_KEY,
        config=GATEWAY_CONFIG_SLUG,
    )

    return ChatOpenAI(
        api_key=config.PORTKEY_API_KEY,
        base_url=PORTKEY_GATEWAY_URL,
        model=config.LLM_MODEL_NAME,
        default_headers=portkey_headers,
    )