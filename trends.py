import requests
import telebot
from data_token import token
import time
import json


def get_news(url):
    r = requests.get(url).text
    data = str(r)[5:].replace('\'', '\\"')
    js = json.loads(data)

    numeral = 0
    list_news = {"urls":[],"titles":[],"data_of_news":[],"source": [], "image" : []}
    while True:
        try:
            urls = js["default"]["trendingSearchesDays"][0]["trendingSearches"][numeral]["image"]["newsUrl"]
            titles = js["default"]["trendingSearchesDays"][0]["trendingSearches"][numeral]["articles"][0]["title"]
            data_of_news = urll = js["default"]["trendingSearchesDays"][0]["date"]
            source = js["default"]["trendingSearchesDays"][0]["trendingSearches"][numeral]["image"]["source"]
            image = js["default"]["trendingSearchesDays"][0]["trendingSearches"][numeral]["image"]["imageUrl"]

            list_news["urls"].append(urls)
            list_news["titles"].append(titles)
            list_news["data_of_news"].append(data_of_news)
            list_news["source"].append(source)
            list_news["image"].append(image)
            numeral += 1
        except:
            print("That`s all")
            break
    return list_news


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands = ["start"])
    def start_message(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
        user_markup.row("/start", "/stop")
        user_markup.row('news')

        bot.send_message(message.from_user.id, "Введите абревиатуру страны поиска:")
        bot.send_message(message.from_user.id, "Австралия - AU\nАвстрия - AT\nАргентина - AR\n"
                                               "Нигерия - NG\nНидерланды - NL\nНовая Зеландия - NZ\nНорвегия - NO\nРеспублика Корея - KR\nРоссийская Федерация - RU\nРумыния - RO\nСаудовская Аравия - SA\nСингапур - SG\n"
                                               "Соединенные Штаты Америки - US\nТаиланд - TH\nТурция - TR\nУкраина - UA\nФилиппины - PH\nФинляндия - FI\nФранция - FR\nЧехия - CZ\nЧили - CL\nШвейцария - CH\n"
                                               "Швеция - SE\nЮжная Африка - ZA\nЯпония - JP\nМалайзия - MY\nМексика - MX\nКанада - CA\nКения - KE\nКолумбия - CO\nПольша - PL\nПортугалия - PT\nИзраиль - IL\n"
                                               "Индия - IN\nИндонезия - ID\nИталия - IT\nИрландия - IE\nБельгия - BE\nБразилия - BR\nВенгрия - HU\nВьетнам - VN\nГермания - DE\nГреция - GR\n"
                                               "Грузия - GE\nГонконг - HK\nДания - DK\nЕгипет - EG\n")

    @bot.message_handler(content_types=["text"])
    def hide_murkup(message):
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, send_text(message), reply_markup = hide_markup)

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        while True:

            if message.text.lower() == "ru":
                country = 'RU'
                bot.send_message(message.from_user.id, "Провожу поиск по Росии...")
                break
            elif message.text.lower() == "us":
                country = "US"
                bot.send_message(message.from_user.id, "Провожу поиск по Америке...")
                break
            elif message.text.lower() == "ua":
                country = "UA"
                bot.send_message(message.from_user.id, "Провожу поиск по Украине...")
                break

            elif message.text.lower() == "jp":
                country = "JP"
                bot.send_message(message.from_user.id, "Провожу поиск по Японии...")
                break

            elif message.text.lower() == "za":
                country = "ZA"
                bot.send_message(message.from_user.id, "Провожу поиск по Южно-Африканской Республике...")
                break


            elif message.text.lower() == "at":
                country = "AT"
                bot.send_message(message.from_user.id, "Провожу поиск по Австрии...")
                break


            elif message.text.lower() == "se":
                country = "SE"
                bot.send_message(message.from_user.id, "Провожу поиск по Швеции...")
                break

            elif message.text.lower() == "ch":
                country = "CH"
                bot.send_message(message.from_user.id, "Провожу поиск по Швейцарии...")
                break


            elif message.text.lower() == "cl":
                country = "CL"
                bot.send_message(message.from_user.id, "Провожу поиск по Чили...")
                break


            elif message.text.lower() == "cz":
                country = "CZ"
                bot.send_message(message.from_user.id, "Провожу поиск по Чехии...")
                break


            elif message.text.lower() == "fr":
                country = "FR"
                bot.send_message(message.from_user.id, "Провожу поиск по Франции...")
                break

            elif message.text.lower() == "fi":
                country = "FI"
                bot.send_message(message.from_user.id, "Провожу поиск по Финляндии...")
                break


            elif message.text.lower() == "ph":
                country = "PH"
                bot.send_message(message.from_user.id, "Провожу поиск по Филипинах...")
                break


            elif message.text.lower() == "tr":
                country = "TR"
                bot.send_message(message.from_user.id, "Провожу поиск по Турции...")
                break


            elif message.text.lower() == "tw":
                country = "TW"
                bot.send_message(message.from_user.id, "Провожу поиск по Тайваню...")
                break


            elif message.text.lower() == "th":
                country = "TH"
                bot.send_message(message.from_user.id, "Провожу поиск по Таиланду...")
                break

            elif message.text.lower() == "sg":
                country = "SG"
                bot.send_message(message.from_user.id, "Провожу поиск по Сингапуре...")
                break


            elif message.text.lower() == "sa":
                country = "SA"
                bot.send_message(message.from_user.id, "Провожу поиск по Саудовской Аравии...")
                break


            elif message.text.lower() == "ro":
                country = "RO"
                bot.send_message(message.from_user.id, "Провожу поиск по Румынии...")
                break


            elif message.text.lower() == "kr":
                country = "KR"
                bot.send_message(message.from_user.id, "Провожу поиск по Республике Корея...")
                break


            elif message.text.lower() == "pt":
                country = "PT"
                bot.send_message(message.from_user.id, "Провожу поиск по Португалии...")
                break


            elif message.text.lower() == "pl":
                country = "PL"
                bot.send_message(message.from_user.id, "Провожу поиск по Польше...")
                break


            elif message.text.lower() == "no":
                country = "NO"
                bot.send_message(message.from_user.id, "Провожу поиск по Норвегии...")
                break


            elif message.text.lower() == "nz":
                country = "NZ"
                bot.send_message(message.from_user.id, "Провожу поиск по Новой Зеландии...")
                break


            elif message.text.lower() == "NL":
                country = "nl"
                bot.send_message(message.from_user.id, "Провожу поиск по Нидерландах...")
                break


            elif message.text.lower() == "ng":
                country = "Ng"
                bot.send_message(message.from_user.id, "Провожу поиск по Нигерии...")
                break


            elif message.text.lower() == "mx":
                country = "MX"
                bot.send_message(message.from_user.id, "Провожу поиск по Мексике...")
                break


            elif message.text.lower() == "my":
                country = "MY"
                bot.send_message(message.from_user.id, "Провожу поиск по Малазии...")
                break


            elif message.text.lower() == "co":
                country = "CO"
                bot.send_message(message.from_user.id, "Провожу поиск по Колумбии...")
                break


            elif message.text.lower() == "ko":
                country = "KO"
                bot.send_message(message.from_user.id, "Провожу поиск по Кении...")
                break


            elif message.text.lower() == "ca":
                country = "CA"
                bot.send_message(message.from_user.id, "Провожу поиск по Канаде...")
                break

            elif message.text.lower() == "it":
                country = "IT"
                bot.send_message(message.from_user.id, "Провожу поиск по Италии...")
                break

            elif message.text.lower() == "ie":
                country = "IE"
                bot.send_message(message.from_user.id, "Провожу поиск по Ирландии...")
                break


            elif message.text.lower() == "sg":
                country = "ID"
                bot.send_message(message.from_user.id, "Провожу поиск по Индонезии ...")
                break

            elif message.text.lower() == "in":
                country = "IN"
                bot.send_message(message.from_user.id, "Провожу поиск по Индии...")
                break


            elif message.text.lower() == "il":
                country = "IL"
                bot.send_message(message.from_user.id, "Провожу поиск по Израилю...")
                break


            elif message.text.lower() == "eg":
                country = "EG"
                bot.send_message(message.from_user.id, "Провожу поиск по Египту...")
                break


            elif message.text.lower() == "dk":
                country = "DK"
                bot.send_message(message.from_user.id, "Провожу поиск по Дании...")
                break


            elif message.text.lower() == "gr":
                country = "GR"
                bot.send_message(message.from_user.id, "Провожу поиск по Греции...")
                break


            elif message.text.lower() == "hk":
                country = "HK"
                bot.send_message(message.from_user.id, "Провожу поиск по Гонконгу...")
                break


            elif message.text.lower() == "de":
                country = "DE"
                bot.send_message(message.from_user.id, "Провожу поиск по Германии...")
                break


            elif message.text.lower() == "vn":
                country = "VN"
                bot.send_message(message.from_user.id, "Провожу поиск по Вьетнаму...")
                break


            elif message.text.lower() == "hu":
                country = "HU"
                bot.send_message(message.from_user.id, "Провожу поиск по Венгрии...")
                break


            elif message.text.lower() == "gb":
                country = "GB"
                bot.send_message(message.from_user.id, "Провожу поиск по Великобритании...")
                break


            elif message.text.lower() == "br":
                country = "BR"
                bot.send_message(message.from_user.id, "Провожу поиск по Бразилии...")
                break


            elif message.text.lower() == "be":
                country = "BE"
                bot.send_message(message.from_user.id, "Провожу поиск по Бельгии...")
                break


            elif message.text.lower() == "ar":
                country = "AR"
                bot.send_message(message.from_user.id, "Провожу поиск по Аргентине...")
                break


            elif message.text.lower() == "at":
                country = "AT"
                bot.send_message(message.from_user.id, "Провожу поиск по Австрии...")
                break


            elif message.text.lower() == "au":
                country = "AU"
                bot.send_message(message.from_user.id, "Провожу поиск по Австралии...")
                break


            else:
                return "Не знаю такой страны ): \nПопробуй ещё разок..."

        url = f"https://trends.google.ru/trends/api/dailytrends?hl=ru&tz=-180&geo={country}&ns=15"

        try:
            links = get_news(url)

            for i in range(len(links["urls"])):
                bot.send_message(message.from_user.id, links["urls"][i])

                time.sleep(2)
            return "Пока что это самые популярные запросы в Гугл в этом регионе..."

        except Exception as ex:
            print(ex)
            bot.send_message(message.chat.id, "Что-то пошло не так...")

    bot.polling(none_stop=True)

def main():
    telegram_bot(token)

if __name__ == "__main__":
    main()