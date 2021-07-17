from typing import Any

from nonebot.adapters.cqhttp import Bot
from nonebot.typing import T_State

from ..matcher import fr24
from ..config import config

from ..libs.info import Info
from ..libs.request import FR24Request

async def now_handler(bot: Bot, state: T_State):
    cmd=state["cmd"]
    if cmd in config.CMDF_NOW:
        request_params = Info.params
        request = FR24Request(Info.real_time_flight_tracker_data_url, request_params, Info.headers)
        response = await request.get_content()
        data = response.json()
        print(response)
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
                    "追踪方式统计：",
                    f"ADS-B:{ads_b}",
                    f"MLAT:{mlat}",
                    f"FAA:{faa}",
                    f"FLARM:{flarm}",
                    f"惯性预测:{estimated}",
                    f"其他：{other}"
        ))
        await fr24.finish(msg,at_sender=True)


