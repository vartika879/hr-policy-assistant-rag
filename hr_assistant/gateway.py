"""Step 6b: route the LLM through the Portkey gateway.

Instead of calling Groq directly, the main LLM call goes through Portkey.
Portkey stores the real Groq credentials behind a "slug" (set up once in
the Portkey dashboard) - our code never sees the raw Groq key.

NOTE on fallback: we used to send a "config" (strategy: fallback + a
list of targets) via the x-portkey-config header, either as inline JSON
or as a saved config's "pc-..." slug. This Portkey workspace has
"block_inline_config" enabled, and there's no saved config to reference
either, so ANY x-portkey-config header - inline or slug - gets rejected
with `inline_config_blocked`. Routing straight to one provider via
x-portkey-provider sidesteps the config mechanism entirely (that header
isn't validated the same way), which is why this version doesn't send a
config at all. The tradeoff: no more automatic Portkey-side fallback to
a second slug if @hrpolicy fails - see docs/05_portkey_gateway.md.
"""


from langchain_openai import ChatOpenAI

from portkey_ai import createHeaders,PORTKEY_GATEWAY_URL

from hr_assistant import config
from hr_assistant.logger import get_logger

logger=get_logger(__name__)

PRIMARY_PROVIDER = "@hr-policy"           # kept for logging/reference only
GATEWAY_CONFIG_SLUG = "pc-hr-pol-d3a682"
 # hr_policy config, v2 — fallback @hr-policy -> @hr-policy-back
"""
def get_gateway_llm() -> ChatOpenAI:
    Return the LLM routed through Portkey.

    logger.info("Routing LLM calls through Portkey (config=%s)", GATEWAY_CONFIG_SLUG)
    headers = createHeaders(
        api_key=config.PORTKEY_API_KEY,
        config=GATEWAY_CONFIG_SLUG,
    )
    return ChatOpenAI(
        api_key=config.PORTKEY_API_KEY,
        base_url=PORTKEY_GATEWAY_URL,
        model=config.LLM_MODEL_NAME,
        default_headers=headers,
    )
"""


def get_gateway_llm() -> ChatOpenAI:
    logger.info(
        "Portkey key configured: %s",
        bool(config.PORTKEY_API_KEY)
    )

    logger.info(
        "Portkey gateway URL: %s",
        PORTKEY_GATEWAY_URL
    )

    logger.info(
        "Portkey config slug: %s",
        GATEWAY_CONFIG_SLUG
    )

    headers = createHeaders(
        api_key=config.PORTKEY_API_KEY,
        config=GATEWAY_CONFIG_SLUG,
    )

    return ChatOpenAI(
        api_key=config.PORTKEY_API_KEY,
        base_url=PORTKEY_GATEWAY_URL,
        model=config.LLM_MODEL_NAME,
        default_headers=headers,
    )
# user
#gateway

# send ,groq,openai,gemini
