from typing import Any

from nonebot.adapters.cqhttp import Bot
from nonebot.typing import T_State
from nonebot.log import logger

from ..matcher import fr24
from ..config import config

from ..libs.info import Info
from ..libs.request import FR24Request

async def now_handler(bot: Bot, state: T_State):
    cmd=state["cmd"]
    if cmd in config.CMDF_NOW:
        request_params = Info.params
        request = FR24Request(Info.real_time_flight_tracker_data_url, request_params, Info.headers)
        try:
            response = await request.get_content()
        except Exception :
            await fr24.finish("端口访问错误或超时，请稍后再试",at_sender=True)
            return
        data = response.json()
        for param, info in data.items():
            if param == "full_count":
                total = info
            if param == "stats":
                stats = info["total"]
                ads_b = stats["ads-b"]
                mlat = stats["mlat"]
                faa = stats["faa"]
                flarm = stats["flarm"]
                estimated = stats["estimated"]
                other = stats["other"]
        msg = '\n'.join((f"当前追踪航班数为:{total}",
        f"追踪方式统计：ADS-B:{ads_b};MLAT:{mlat};FAA:{faa};FLARM:{flarm};惯性预测:{estimated};其他:{other}"
        ))
        await fr24.finish(msg,at_sender=True)


