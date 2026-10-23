"""NoneBot 命令、统一会话和消息；业务由生成的共享运行时处理。"""

import logging

from nonebot import get_driver, get_plugin_config, on_command
from nonebot.adapters import Bot, Event, Message
from nonebot.params import CommandArg
from nonebot_plugin_alconna import At, UniMessage
from nonebot_plugin_alconna.uniseg import get_message_id
import nonebot_plugin_localstore as store
from nonebot_plugin_uninfo import Uninfo

from .config import Config
from .data_paths import data_directory
from .runtime import Runtime, command_map

COMMANDS = command_map('nonebot')

logger = logging.getLogger(__name__)
config = get_plugin_config(Config)
driver = get_driver()
runtime = Runtime(
    data_directory(store.get_plugin_data_dir(), config.farm_data_dir),
    config.farm_font, config.farm_deployment, config.farm_image_format,
    font_setting="FARM_FONT",
    image_quality=config.farm_image_quality,
    framework='nonebot',
    resource_source=config.farm_resource_source,
    service_url=config.farm_service_url,
)
driver.on_startup(runtime.start)
driver.on_shutdown(runtime.close)


def handler_for(action):
    async def handle(
        bot: Bot, event: Event, session: Uninfo,
        args: Message = CommandArg(),
    ):
        try:
            message_id = get_message_id(event, bot)
        except Exception:
            message_id = None
        try:
            target_user_id = None
            if action == "steal":
                mentions = UniMessage.of(args, bot=bot)[At]
                if len(mentions) != 1 or mentions[0].flag != "user":
                    await UniMessage("请只@一个具体偷菜目标。").send(
                        event, bot, reply_to=bool(message_id),
                    )
                    return
                target_user_id = mentions[0].target
            response = await runtime.execute(
                action, args.extract_plain_text(),
                bot_id=str(bot.self_id), platform=bot.adapter.get_name(),
                user_id=str(session.user.id), message_id=message_id,
                display_name=session.user.name or "农场玩家",
                target_user_id=target_user_id,
            )
        except Exception as error:
            logger.error("farm request failed type=%s", type(error).__name__)
            response = "农场服务异常，请查看服务器日志。"
        message = (UniMessage.image(raw=response)
                   if isinstance(response, bytes) else UniMessage(response))
        await message.send(event, bot, reply_to=bool(message_id))
    return handle


for command, action in COMMANDS.items():
    matcher = on_command(command, priority=5, block=True)
    matcher.handle()(handler_for(action))
