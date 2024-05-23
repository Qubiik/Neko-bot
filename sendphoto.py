import telebot
import os
def handle_photo(message):
    TOKEN = "7110857454:AAF97VdQ31Pa2G0dsvbc-Gb7ESnalm4zj_g"

    bot = telebot.TeleBot(TOKEN)

    # Создаем папку 'neko', если её нет
    if not os.path.exists('neko'):
        os.makedirs('neko')

    # Получаем информацию о файле
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    file_extension = '.' + file_info.file_path.split('.')[-1]

    # Находим порядковый номер для нового файла
    files = os.listdir('neko')
    file_numbers = [int(file.split('.')[0]) for file in files if file.split('.')[0].isdigit()]
    if file_numbers:
        next_file_number = max(file_numbers) + 1
    else:
        next_file_number = 1

    # Сохраняем файл в папку 'neko'
    downloaded_file = bot.download_file(file_info.file_path)
    with open(f'neko/{next_file_number}{file_extension}', 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.reply_to(message, "Фото сохранено!")
if __name__ == "__main__":
    TOKEN = "7110857454:AAF97VdQ31Pa2G0dsvbc-Gb7ESnalm4zj_g"
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(content_types=['photo'])
    def handle_incoming_message(message):
        handle_photo(message)

    bot.polling()
