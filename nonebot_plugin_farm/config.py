from pathlib import Path
from nonebot import require
from nonebot.plugin import get_plugin_config
from pydantic import BaseModel

require("nonebot_plugin_localstore")

import nonebot_plugin_localstore as store

# 签到状态
g_bSignStatus = True

# 是否处于Debug模式
g_bIsDebug = True

# 数据库文件目录
g_sDBPath = store.get_plugin_data_dir() / "nonebot_plugin_farm/farm_db"

# 数据库文件路径
g_sDBFilePath = g_sDBPath / "farm.db"

# 农场资源文件目录
g_sResourcePath = Path(__file__).resolve().parent / "resource"

# 农场作物数据库
g_sPlantPath = g_sResourcePath / "db/plant.db"

# 农场配置文件目录
g_sConfigPath = Path(__file__).resolve().parent / "config"

# 农场签到文件路径
g_sSignInPath = g_sConfigPath / "sign_in.json"


class Config(BaseModel):
    farm_draw_quality: str = "low"
    farm_server_url: str = "http://diuse.work"


g_pConfigManager = get_plugin_config(Config)
