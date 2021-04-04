from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton


def buttons(text):
    menu = InlineKeyboardMarkup(row_width=2)
    if text:
        butt = InlineKeyboardButton(
            text=f"📹 Смотреть {text} урок >", callback_data=text)
        menu.add(butt)
    butt = InlineKeyboardButton(text="💳 Купить полный курс >",
                                url="https://capu.st/bill9922b262-32ac")
    menu.add(butt)

    return menu
