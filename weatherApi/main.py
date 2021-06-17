# from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update
# from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext, MessageHandler, Filters
# from pyowm import OWM
# from telegram.ext.filters import Filters
# from telegram.update import Update
# 
# owm = OWM("8b5af2e17b3d8d588b0a025f3bf4373f")
# mgr = owm.weather_manager()
# 
# updater = Updater(token="1888524272:AAGU2mwlWFKVVVS6jg9IXOTSF2lQbFco1KU")
# 
# 
# def start(update: Update, context: CallbackContext):
#     update.message.reply_text("Assalomu aleykum!, ob-havo bot ga xush kelibsiz, masalan shunday yozing /search Tashkent Uzbekistan")
# 
# 
# def search(update: Update, context: CallbackContext):
#     args = context.args
#     if len(args) == 0:
#         update.message \
#             .reply_text('Hech bo‘lmasa, nimadir kiriting. Misol uchun '
#                         '/search Tashkent Uzbekistan')
#     else:
#         search_txt = args
#         print(search_txt)
#         observation = mgr.weather_at_place(search_txt[0]+','+search_txt[1])
#         w = observation.weather
#         print(w.temperature('celsius'))
# 
#         update.message.reply_text(f"<b>🏙 Shaxar:</b> {search_txt[0]}\n"
#                                   f"<b>🌡 Harorat:</b> {str(round(w.temperature('celsius').get('temp')))}°\n"
#                                   f"<b>💨 Shamol tezligi:</b> {str(w.wind().get('speed'))} m/s\n"
#                                   f"<b>💦 Havo namligi:</b> {str(w.humidity)}%",
#                                   parse_mode=ParseMode.HTML)
# 
# 
# dispatcher = updater.dispatcher
# dispatcher.add_handler(CommandHandler('start', start))
# dispatcher.add_handler(CommandHandler('search', search))
# 
# 
# updater.start_polling()
# updater.idle()
# 
# # w.detailed_status         # 'clouds'
# # w.wind()                  # {'speed': 4.6, 'deg': 330}
# # w.humidity                # 87
# # w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# # w.rain                    # {}
# # w.heat_index              # None
# # w.clouds                  # 75
# 
# # # Will it be clear tomorrow at this time in Milan (Italy) ?
# # forecast = mgr.forecast_at_place('Milan,IT', 'daily')
# # answer = forecast.will_be_clear_at(timestamps.tomorrow())
from telegram import InlineKeyboardButton, InlineKeyboardMarkup # This helps us to create 
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler


def start(update, context):
    user = update.message.from_user['first_name']
    update.message.reply_html(f"Assalomu Aleykum <b>{user}!</b>\n \n<b>Ramazon oyi muborak bo'lsin!</b>\n \nSizga qaysi mintaqa bo'yicha ma'lumot beray")


def main():
    # Setting up the updater
    updater = Updater('1894288182:AAE4rHwA2V_4-2463mXg6dTl6P-D955mcUk', use_context=True)

    # Dispatcher to handle events
    dispatcher = updater.dispatcher

    # /start command
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.all, start))

    updater.start_polling()
    updater.idle()


main()
