LEXICON: dict[str, str] = {
    'forward': '>>',
    'backward': '<<',
    '/start': '<b>Привет, читатель!</b>\n\nЭто бот, в котором '
              'ты можешь прочитать книгу Рэя Брэдбери "Марсианские '
              'хроники"\n\nЧтобы просмотреть список доступных '
              'команд - набери /help',
    '/help': '<b> Этобот-читалка</b>\n\nДоступные команды:\n\n/beginning - '
             'перейти в начало книги\n/continue - продолжить '
             'чтение\n/bookmarks - посмотреть список закладок\n/help - '
             'справка по работе бота\n\nЧтобы сохранить закладку - '
             'нажмите на кнопку с номером страницы\n\n<b>Приятного чтения!</b>',
    '/bookmarks': '<b>Это список ваших закладок:</b>',
    'edit_bookmarks': '<b>Редактироватьзакладки</b>',
    'edit_bookmarks_button': '❌РЕДАКТИРОВАТЬ',
    'del': '❌',
    'cancel': 'ОТМЕНИТЬ',
    'no_bookmarks': 'У вас пока нет ниодной закладки.\n\nЧтобы '
                    'добавить страницу в закладки - во время чтения '
                    'книги нажмите на кнопку с номером этой '
                    'страницы\n\n/continue - продолжить чтение',
    'cancel_text': '/continue - продолжить чтение'
}

LEXICON_COMMANDS: dict[str,str] = {
    '/beginnig': 'В началокниги',
    '/continue': 'Продолжить чтение',
    '/bookmarks': 'Мои закладки',
    '/help': 'Справка по работе бота'
}
