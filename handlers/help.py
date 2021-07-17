from typing import Any

from nonebot.adapters.cqhttp import Bot
from nonebot.typing import T_State

from ..config import config
from ..matcher import fr24


async def help_handler(bot: Bot, state: T_State) -> Any:
    cmd = state['cmd']
    if cmd in config.CMDF_HELP:
        await fr24.finish('\n'.join((
            "FlightRadar24查询，以 \"/fr24\" 开头：\n",
            "/fr24 help 帮助",
            "/fr24 now 查看当前航空器",
            "其他功能请等待后续开发~"      
        )))
        return