"""兼容旧版 NoneBot localstore 存档位置。"""

from pathlib import Path


def data_directory(base, configured=None):
    if configured is not None:
        return Path(configured)
    return Path(base) / "nonebot_plugin_farm" / "farm_db"
