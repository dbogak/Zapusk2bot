from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from aiogram import md
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from loader import dp, bot
import menu
import asyncio

id_photo = 'AgACAgIAAxkBAAMEYGcx45NIiXnGOFTxY_g3RVu_4p4AAkOxMRubvjlL-AmC9GgJd4qSgY-eLgADAQADAgADeQADo5MAAh4E'
vid1 = 'BAACAgIAAxkBAAMkYGdGS9ZrzP7p3NxkNCFaaKP5uxcAAigNAAIEY0BLSlnLUJNY2q8eBA'
vid2 = 'BAACAgIAAxkBAAMsYGdQKE8TKiAxAjLl6peVeAZS4aAAAkENAAIEY0BLkcSbA617VaoeBA'
cap = '''Привет, это бот курса “Кухня запусков 2.0”

Здесь вы можете купить полный курс со всеми видео, презентациям, ДЗ и тд)

Для большей достоверности, нажмите на кнопку “Получить урок” и вы получите первый урок курса бесплатно!
'''
cap1 = 'Это первый урок, в ускоренном формате, смотрите и получайте пользу) Вы можете купить полный курс по кнопке “Купить полный курс” или получить еще один урок по кнопке “Еще урок”)'
cap2 = 'Уже второй урок в ускоренном формате для вас бесплатно) Вы также можете купить полный курс по кнопке “Купить полный курс” или получить последний, третий бесплатный урок) все так же по кнопке “Еще урок)” '
cap3 = 'Это был последний урок из серии бесплатных уроков, прямо сейчас вы можете купить полный курс для запуска инфопродуктов в интернете, купить курс и получить доступ к полному курсу > Ссылка на оплату'


@dp.message_handler(Command("start"))
async def com_start(message: Message):
    """ ==== Команда start в боте для всех ==== """
    await message.answer(f'Здравствуйте {message.from_user.full_name}', reply_markup=ReplyKeyboardRemove(True))
    await message.answer_photo(id_photo, caption=cap, reply_markup=menu.buttons(text="Первый"))


@dp.callback_query_handler(text_contains="Первый")
async def link(call: CallbackQuery):
    print('Первый урок')
    await call.message.answer_video(vid1, caption=cap1, reply_markup=menu.buttons(text="Второй"))


@ dp.callback_query_handler(text_contains="Второй")
async def link2(call: CallbackQuery):
    print('Второй урок')
    await call.message.answer_video(vid2, caption=cap2, reply_markup=menu.buttons(text="Третий"))


@ dp.callback_query_handler(text_contains="Третий")
async def link3(call: CallbackQuery):
    print('Третий урок')
    await call.message.answer_video(vid2, caption=cap3, reply_markup=menu.buttons(text=None))
    await asyncio.sleep(3600*3)
    await call.message.answer('А вот и ссылка. Че мне прислали то и я отправляю')


@ dp.message_handler(content_types=["photo"])
async def linkus(message: Message, state: FSMContext):
    await message.answer(message.photo[1].file_id)


@ dp.message_handler(content_types=["video"])
async def aa(message: Message, state: FSMContext):
    await message.answer(message.video.file_id)
