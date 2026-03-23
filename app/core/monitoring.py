import logging
from app.config.settings import settings
from app.utils.azure_secrets import get_secret

logger = logging.getLogger("app")


def setup_monitoring():
    if settings.ENV == "prod":
        from opencensus.ext.azure.log_exporter import AzureLogHandler

        logger.addHandler(
            AzureLogHandler(connection_string=get_secret("APPINSIGHTS_CONNECTION_STRING"))
        )

    logger.setLevel(settings.LOG_LEVEL)
