"""普通 NoneBot 农场插件入口。"""

from nonebot import require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_plugin_alconna")
require("nonebot_plugin_uninfo")
require("nonebot_plugin_localstore")

from ._version import __version__
from .config import Config
from .runtime import command_specs, help_text

__plugin_meta__ = PluginMetadata(
    name="农场", description="快乐的农场时光",
    usage=help_text(command_specs('nonebot')),
    type="application", config=Config,
    homepage="https://github.com/Shu-Ying/nonebot_plugin_farm",
    supported_adapters=inherit_supported_adapters(
        "nonebot_plugin_alconna", "nonebot_plugin_uninfo",
    ),
    extra={"author": "Shu-Ying", "version": __version__},
)

from . import commands
