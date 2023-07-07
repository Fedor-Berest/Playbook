from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup


def get_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    kb.add('Регби 15', 'Регби 7')

    return kb


def get_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=2)
    ib_1 = InlineKeyboardButton(text='Нападающие', callback_data='forwards')
    ib_2 = InlineKeyboardButton(text='Четверть', callback_data='quarter')
    ib_3 = InlineKeyboardButton(text='<<Назад>>', callback_data='back')
    ikb.add(ib_1, ib_2, ib_3)

    return ikb


def get_ikb_quarter() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    ib_1 = InlineKeyboardButton(text='Самолет', callback_data='combination_quarter_1_1')
    ib_2 = InlineKeyboardButton(text='Драный Хвост', callback_data='combination_quarter_2_1')
    ib_3 = InlineKeyboardButton(text='Короток', callback_data='combination_quarter_3_1')
    ib_4 = InlineKeyboardButton(text='Прокол', callback_data='combination_quarter_4_1')
    ib_5 = InlineKeyboardButton(text='Кеник', callback_data='combination_quarter_5_1')
    ib_6 = InlineKeyboardButton(text='Ларек', callback_data='combination_quarter_6_1')
    ib_7 = InlineKeyboardButton(text='Магазин', callback_data='combination_quarter_7_1')
    ib_8 = InlineKeyboardButton(text='<<Назад>>', callback_data='back_position')
    ikb.add(ib_1, ib_2, ib_3, ib_4, ib_5, ib_6, ib_7, ib_8)

    return ikb


def get_ikb_quarter_1() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    ib_1 = InlineKeyboardButton(text='Самолет - 1', callback_data='combination_quarter_1_1')
    ib_2 = InlineKeyboardButton(text='Самолет - 2', callback_data='combination_quarter_1_2')
    ib_3 = InlineKeyboardButton(text='Самолет - 3', callback_data='combination_quarter_1_3')
    ib_4 = InlineKeyboardButton(text='Самолет - 4', callback_data='combination_quarter_1_4')
    ib_5 = InlineKeyboardButton(text='<<Назад>>', callback_data='quarter')
    ikb.add(ib_1, ib_2, ib_3, ib_4, ib_5)

    return ikb


def get_ikb_quarter_2() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    ib_1 = InlineKeyboardButton(text='Драный хвост - 1', callback_data='combination_quarter_2_1')
    ib_2 = InlineKeyboardButton(text='Драный хвост - 2', callback_data='combination_quarter_2_2')
    ib_3 = InlineKeyboardButton(text='Драный хвост - 3', callback_data='combination_quarter_2_3')
    ib_4 = InlineKeyboardButton(text='Драный хвост - 4', callback_data='combination_quarter_2_4')
    ib_5 = InlineKeyboardButton(text='Драный хвост - 5', callback_data='combination_quarter_2_5')
    ib_6 = InlineKeyboardButton(text='<<Назад>>', callback_data='quarter')
    ikb.add(ib_1, ib_2, ib_3, ib_4, ib_5, ib_6)

    return ikb


def get_ikb_quarter_3() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    ib_1 = InlineKeyboardButton(text='Короток - 1', callback_data='combination_quarter_3_1')
    ib_2 = InlineKeyboardButton(text='Короток - 2(спина)', callback_data='combination_quarter_3_2')
    ib_3 = InlineKeyboardButton(text='<<Назад>>', callback_data='quarter')
    ikb.add(ib_1, ib_2, ib_3)

    return ikb


def get_ikb_quarter_4() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    ib_1 = InlineKeyboardButton(text='Прокол - 1', callback_data='combination_quarter_4_1')
    ib_2 = InlineKeyboardButton(text='Прокол - 2(спина)', callback_data='combination_quarter_4_2')
    ib_3 = InlineKeyboardButton(text='<<Назад>>', callback_data='quarter')
    ikb.add(ib_1, ib_2, ib_3)

    return ikb


def get_ikb_quarter_5() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    ib_1 = InlineKeyboardButton(text='Кеник - 1', callback_data='combination_quarter_5_1')
    ib_2 = InlineKeyboardButton(text='Кеник - 2', callback_data='combination_quarter_5_2')
    ib_3 = InlineKeyboardButton(text='<<Назад>>', callback_data='quarter')
    ikb.add(ib_1, ib_2, ib_3)

    return ikb


def get_ikb_quarter_6() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    ib_1 = InlineKeyboardButton(text='Ларек - 1', callback_data='combination_quarter_6_1')
    ib_2 = InlineKeyboardButton(text='Ларек - 2(внутрь)', callback_data='combination_quarter_6_2')
    ib_3 = InlineKeyboardButton(text='<<Назад>>', callback_data='quarter')
    ikb.add(ib_1, ib_2, ib_3)

    return ikb


def get_ikb_quarter_7() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    ib_1 = InlineKeyboardButton(text='Магазин - 1', callback_data='combination_quarter_7_1')
    ib_2 = InlineKeyboardButton(text='Магазин - 2(внутрь)', callback_data='combination_quarter_7_2')
    ib_3 = InlineKeyboardButton(text='<<Назад>>', callback_data='quarter')
    ikb.add(ib_1, ib_2, ib_3)

    return ikb


def get_ikb_forwards() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    ib_1 = InlineKeyboardButton(text='Жук', callback_data='combination_forwards_1_1')
    ib_2 = InlineKeyboardButton(text='<<Назад>>', callback_data='back_position')
    ikb.add(ib_1, ib_2)

    return ikb


def get_ikb_forwards_1() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    ib_1 = InlineKeyboardButton(text='Жук - 1', callback_data='combination_forwards_1_1')
    ib_2 = InlineKeyboardButton(text='Жук - 2', callback_data='combination_forwards_1_2')
    ib_3 = InlineKeyboardButton(text='<<Назад>>', callback_data='forwards')
    ikb.add(ib_1, ib_2, ib_3)

    return ikb
