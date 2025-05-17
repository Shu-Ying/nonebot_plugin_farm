from pathlib import Path
from nonebot import require
from nonebot.plugin import get_plugin_config
from pydantic import BaseModel

import nonebot_plugin_localstore as store


g_sDBPath = store.get_plugin_data_dir() / "nonebot_plugin_farm/farm_db"
g_sDBFilePath = g_sDBPath / "farm.db"

g_sResourcePath = Path(__file__).resolve().parent / "resource"

g_sPlantPath = g_sResourcePath / "db/plant.db"

class Config(BaseModel):
    farm_draw_quality: str = "low"
    farm_server_url: str = "http://diuse.work"

g_pConfigManager = get_plugin_config(Config)