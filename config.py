from typing import Any
from copy import deepcopy
from pydantic import BaseSettings

import nonebot

class Config(BaseSettings):
    _config: Any = deepcopy(nonebot.get_driver().config)

    CMD: str       = 'fr24'    # 响应指令
    ALIASES: set   = { 'f' }  # 命令的 aliases
    CMD_START: str = list(_config.command_start)[0]
    CMD_SEP: str   = list(_config.command_sep)[0]

    CMDF_HELP: set   = { 'help', 'doc', '帮助' }
    CMDF_NOW: set    = { 'now', '实时' }
    CMDF_TYPE: set   = { 'type', '机型' }
    CMDF_FROM: set   = { 'from', '出发' }
    CMDF_TO: set     = { 'to', '到达' }
    CMDF_AIRLINE: set ={'air', '公司'}
    CMDF_FLIGHT : set ={'flight', '航班'}
    TIMEOUT = 5

config = Config()
