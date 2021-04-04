import logging
from config import BOT_TOKEN

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
#from locales.language_middleware import setup_middleware

class Usr:
    groups = {}
    select_group = {}

bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

#i18n = setup_middleware(dp)
#_ = i18n.gettext

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    )
