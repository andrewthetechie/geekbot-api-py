from .clients.reports import _ReportClient
from .clients.standups import _StandupClient
from .clients.teams import _TeamClient
from .config import GeekbotAPIConfig


class GeekbotAPIClient:
    def __init__(self, config: GeekbotAPIConfig):
        self.config = config
        self.teams = _TeamClient(
            base_api_path=config.base_api_path,
            api_version=config.api_version,
            path="teams/",
            api_key=config.api_key,
        )
        self.reports = _ReportClient(
            base_api_path=config.base_api_path,
            api_version=config.api_version,
            path="reports/",
            api_key=config.api_key,
        )
        self.standups = _StandupClient(
            base_api_path=config.base_api_path,
            api_version=config.api_version,
            path="standups/",
            api_key=config.api_key,
        )
