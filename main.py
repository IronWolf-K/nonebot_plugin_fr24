from .matcher import fr24
from . import handlers

fr24.handle()(handlers.pre_handler)
fr24.handle()(handlers.help_handler)
fr24.handle()(handlers.now_handler)
fr24.handle()(handlers.filter_handler)