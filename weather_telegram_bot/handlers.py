import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.filters import CommandStart


bot = Bot(token=tg_bot_token)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды!")


@dp.message()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.reply(f"<b>---{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}---</b>\n"
              f"<b>Погода в городе:</b> {city}"
              f"\n<b>Температура:</b> <code>{cur_weather}C°</code> {wd}\n"
              f"<b>Влажность:</b> <code>{humidity}%</code>"
              f"\n<b>Давление:</b> <code>{pressure} мм.рт.ст</code>\n"
              f"<b>Ветер:</b> <code>{wind} м/с</code>\n"
              f"<b>Восход солнца:</b> <code>{sunrise_timestamp}</code>"
              f"\n<b>Закат солнца:</b> <code>{sunset_timestamp}</code>\n"
              f"<b>Продолжительность дня:</b> <code>{length_of_the_day}</code>\n"
              f"<b>---Хорошего дня!---</b>",
              parse_mode='HTML')

    except:
        await message.reply("\U00002620 Проверьте название города \U00002620")

if __name__ == "__main__":
    dp.run_polling(bot)
