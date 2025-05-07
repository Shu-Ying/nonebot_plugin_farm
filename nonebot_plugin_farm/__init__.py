from nonebot import get_driver
from nonebot.plugin import PluginMetadata

from nonebot import logger

from .command import diuse_farm, diuse_register, reclamation
from .config import g_pConfigManager
from .json import g_pJsonManager
from .database.database import g_pSqlManager
from .dbService import g_pDBService
from .farm.farm import g_pFarmManager
from .farm.shop import g_pShopManager
from .request import g_pRequestManager

__plugin_meta__ = PluginMetadata(
    name="真寻农场",
    description="快乐的农场时光",
    usage="""
    你也要种地?
    指令：
        at 开通农场
        我的农场
        我的农场币
        种子商店 [页数]
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
    """.strip()
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

# 析构函数
@driver.on_shutdown
async def shutdown():
    await g_pSqlManager.cleanup()
