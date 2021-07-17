from nonebot.plugin import on_shell_command
from nonebot.rule import ArgumentParser
from .config import config
def get_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument('cmd')
    return parser

fr24 = on_shell_command(
    cmd=config.CMD,
    aliases=set(map(lambda x: x + ' ', config.ALIASES)),
    parser=get_parser()
)