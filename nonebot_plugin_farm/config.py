from nonebot.plugin import get_plugin_config
from pydantic import BaseModel

from pathlib import Path

g_sDBPath = Path(__file__).resolve().parent / "farm_db"
g_sDBFilePath = Path(__file__).resolve().parent / "farm_db/farm.db"

g_sResourcePath = Path(__file__).resolve().parent / "resource"


class Config(BaseModel):
    farm_draw_quality: str = "low"
    farm_server_url: str = "http://diuse.work"

g_pConfigManager = get_plugin_config(Config)
