from nonebot import get_driver, logger, require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

from .config import Config

require("nonebot_plugin_alconna")
require("nonebot_plugin_uninfo")
require("nonebot_plugin_waiter")
require("nonebot_plugin_apscheduler")


from nonebot_plugin_apscheduler import scheduler

from .command import diuse_farm, diuse_register, reclamation
from .config import g_pConfigManager
from .database.database import g_pSqlManager
from .dbService import g_pDBService
from .farm.farm import g_pFarmManager
from .farm.shop import g_pShopManager
from .json import g_pJsonManager
from .request import g_pRequestManager

__plugin_meta__ = PluginMetadata(
    name="真寻农场",
    description="快乐的农场时光",
    usage="""
    你也要种地?
    指令：
        at 开通农场
        我的农场
        农场详述
        我的农场币
        种子商店 [筛选关键字] [页数] or [页数]
        购买种子 [作物/种子名称] [数量]
        我的种子
        播种 [作物/种子名称] [数量] (数量不填默认将最大可能播种
        收获
        铲除
        我的作物
        出售作物 [作物/种子名称] [数量] (不填写作物名将售卖仓库种全部作物 填作物名不填数量将指定作物全部出售
        偷菜 at (每人每天只能偷5次
        开垦
        购买农场币 [数量] 数量为消耗金币的数量
        更改农场名 [新农场名]
        农场签到
        土地升级 [地块ID]（通过农场详述获取）
    """.strip(),
    type="application",
    homepage="https://github.com/Shu-Ying/nonebot_plugin_farm",
    config=Config,
    supported_adapters=inherit_supported_adapters(
        "nonebot_plugin_alconna",
        "nonebot_plugin_uninfo",
        "nonebot_plugin_waiter",
        "nonebot_plugin_localstore",
        "nonebot_plugin_apscheduler",
    ),
)
driver = get_driver()


# 构造函数
@driver.on_startup
async def start():
    # 初始化数据库
    await g_pSqlManager.init()

    # 初始化读取Json
    await g_pJsonManager.init()

    await g_pDBService.init()

    # 检查作物文件是否缺失 or 更新
    await g_pRequestManager.initPlantDBFile()


# 析构函数
@driver.on_shutdown
async def shutdown():
    await g_pSqlManager.cleanup()

    await g_pDBService.cleanup()


@scheduler.scheduled_job(trigger="cron", hour=4, minute=30, id="signInFile")
async def signInFile():
    try:
        await g_pJsonManager.initSignInFile()
        await g_pRequestManager.initPlantDBFile()
    except Exception as e:
        logger.error("农场定时检查出错", e=e)
