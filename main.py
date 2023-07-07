from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
from keyboards import get_kb, get_ikb, get_ikb_quarter, get_ikb_forwards, get_ikb_quarter_1, get_ikb_quarter_2,\
    get_ikb_quarter_3, get_ikb_quarter_4, get_ikb_quarter_5, get_ikb_quarter_6, get_ikb_quarter_7, get_ikb_forwards_1


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Добро пожаловть в телеграм бот с комбинациями регбийного клуба приморец.\n'
                         'Для начала выберите комбинации по какому виду регби вы хотите увидеть',
                         reply_markup=get_kb())


@dp.callback_query_handler()
async def callback_handler(callback: types.CallbackQuery) -> None:
    print(callback.from_user.values['first_name'], callback.from_user.values['username'])
    if callback.data == 'forwards':
        await bot.send_message(chat_id=callback.message.chat.id,
                               text='Вот комбинации нападающих',
                               reply_markup=get_ikb_forwards())

    elif callback.data == 'quarter':
        await bot.send_message(chat_id=callback.message.chat.id,
                               text='Вот комбинации четверти',
                               reply_markup=get_ikb_quarter())

    elif callback.data == 'back':
        await bot.send_message(chat_id=callback.message.chat.id,
                               text='Добро пожаловть в телеграм бот с комбинациями регбийного клуба приморец.\n'
                                    'Для начала выберите комбинации по какому виду регби вы хотите увидеть',
                               reply_markup=get_kb())

    elif callback.data == 'back_position':
        await bot.send_message(chat_id=callback.message.chat.id,
                               text='Далее выберите комбинации нападающих или четвертных вы хотите увидеть',
                               reply_markup=get_ikb())

    elif 'combination_quarter_1' in callback.data:
        if callback.data == 'combination_quarter_1_1':
            with open('video/quarter/самолет/самолет 1.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Самолет"\nСуществует 4 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_quarter_1())

        elif callback.data == 'combination_quarter_1_2':
            with open('video/quarter/самолет/самолет 2.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Самолет 2"\nСуществует 4 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_quarter_1())

        elif callback.data == 'combination_quarter_1_3':
            with open('video/quarter/самолет/самолет 3.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Самолет 3"\nСуществует 4 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_quarter_1())

        elif callback.data == 'combination_quarter_1_4':
            with open('video/quarter/самолет/самолет 4.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Самолет 4"\nСуществует 4 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_quarter_1())


    elif 'combination_quarter_2' in callback.data:
        if callback.data == 'combination_quarter_2_1':
            with open('video/quarter/драный квост/драный хвост 1.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Драный хвост 1"\nСуществует 5 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_quarter_2())

        elif callback.data == 'combination_quarter_2_2':
            with open('video/quarter/драный квост/драный хвост 2.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Драный хвост 2"\nСуществует 5 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_quarter_2())

        elif callback.data == 'combination_quarter_2_3':
            with open('video/quarter/драный квост/драный хвост 3.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Драный хвост 3"\nСуществует 5 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_quarter_2())

        elif callback.data == 'combination_quarter_2_4':
            with open('video/quarter/драный квост/драный хвост 4.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Драный хвост 4"\nСуществует 5 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_quarter_2())

        elif callback.data == 'combination_quarter_2_5':
            with open('video/quarter/драный квост/драный хвост 5.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Драный хвост 5(сменка)"\nСуществует 5 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_quarter_2())


    elif 'combination_quarter_3' in callback.data:
        if callback.data == 'combination_quarter_3_1':
            with open('video/quarter/короток/короток 1.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Короток 1"\nСуществует 2 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_quarter_3())

        elif callback.data == 'combination_quarter_3_2':
            with open('video/quarter/короток/короток 2.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Короток 2(спина)"\nСуществует 2 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_quarter_3())


    elif 'combination_quarter_4' in callback.data:
        if callback.data == 'combination_quarter_4_1':
            with open('video/quarter/прокол/прокол 1.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Прокол 1"\nСуществует 2 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_quarter_4())

        elif callback.data == 'combination_quarter_4_2':
            with open('video/quarter/прокол/прокол 2.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Прокол 2(спина)"\nСуществует 2 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_quarter_4())


    elif 'combination_quarter_5' in callback.data:
        if callback.data == 'combination_quarter_5_1':
            with open('video/quarter/кеник/кеник 1.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Кеник 1"\nСуществует 2 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_quarter_5())

        elif callback.data == 'combination_quarter_5_2':
            with open('video/quarter/кеник/кеник 2.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Кеник 2"\nСуществует 2 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_quarter_5())


    elif 'combination_quarter_6' in callback.data:
        if callback.data == 'combination_quarter_6_1':
            with open('video/quarter/ларек/ларек 1.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Ларек 1"\nСуществует 2 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_quarter_6())

        elif callback.data == 'combination_quarter_6_2':
            with open('video/quarter/ларек/ларек 2.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Ларек 2(внутрь)"\nСуществует 2 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_quarter_6())


    elif 'combination_quarter_7' in callback.data:
        if callback.data == 'combination_quarter_7_1':
            with open('video/quarter/магазин/магазин 1.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Магазин 1"\nСуществует 2 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_quarter_7())

        elif callback.data == 'combination_quarter_7_2':
            with open('video/quarter/магазин/магазин 2.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Магазин 2(внутрь)"\nСуществует 2 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_quarter_7())


    elif 'combination_forwards_1' in callback.data:
        if callback.data == 'combination_forwards_1_1':
            with open('video/forwards/жук/жук 1.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Жук"\nСуществует 2 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_forwards_1())

        elif callback.data == 'combination_forwards_1_2':
            with open('video/forwards/жук/жук 2.mp4', 'rb') as video:
                await bot.send_video(chat_id=callback.message.chat.id,
                                     video=video,
                                     caption='Комбинация - "Жук 2"\nСуществует 2 вариации в зависимости от ситуации на поле:',
                                     reply_markup=get_ikb_forwards_1())


@dp.message_handler()
async def text_button(message: types.Message) -> None:
    if message.text == 'Регби 15':
        await message.answer('Далее выберите комбинации нападающих или четвертных вы хотите увидеть',
                             reply_markup=get_ikb())
    elif message.text == 'Регби 7':
        await message.answer('К сожалению, комбинаций по регби 7 пока нет',
                             reply_markup=get_kb())
    elif message.text == 'Назад':
        await message.answer('Добро пожаловть в телеграм бот с комбинациями регбийного клуба приморец.\n'
                             'Для начала выберите комбинации по какому из видов регби вы хотите увидеть',
                             reply_markup=get_kb())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)