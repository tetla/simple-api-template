import os
from logging import getLogger

logger = getLogger(__name__)

class APIConfigurations:
    title = os.getenv("API_TITLE", "SimpleAPI")
    description = os.getenv("API_DESCRIPTION", "simple api template")
    version = os.getenv("API_VERSION", "0.1")

logger.info(f"{APIConfigurations.__name__}: {APIConfigurations.__dict__}")

