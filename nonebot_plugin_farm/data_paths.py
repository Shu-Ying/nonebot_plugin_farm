"""兼容旧版 NoneBot localstore 存档位置。"""

from pathlib import Path


def data_directory(base, configured=None):
    if configured:
        return Path(configured).expanduser()
    return Path(base) / "nonebot_plugin_farm" / "farm_db"
