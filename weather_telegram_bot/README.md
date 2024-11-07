# Weather Bot

Этот проект представляет собой Telegram-бота, который предоставляет сводку погоды для указанного пользователем города. Бот использует API OpenWeatherMap для получения данных о текущей погоде и отображает её в удобном формате.

## Структура проекта

- **config.py** — содержит настройки токенов для работы с API OpenWeatherMap и Telegram.
- **handlers.py** — содержит логику обработки команд и получения данных о погоде, а также отправку ответа пользователю.

## Код создан на основе IDeF0 диаграммы

[ccылка на диаграмму](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=weather_bot.drawio#R%3Cmxfile%3E%3Cdiagram%20name%3D%22%D0%A1%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0%20%E2%80%94%201%22%20id%3D%22m3OpFU5KmMsNH2Q8RI0B%22%3E7Vxbc5s4FP41PDaDuPNoG3u7M91pZtqdbh%2BJrdhsMXgxSZz%2B%2BhUgyUcXbHzBTur2gYIshDjnfOdODHu03PxRxKvFX%2FkMp4ZlzjaGHRmWhXzbJ%2F9VI6%2FNSOi6zcC8SGZ00nbgS%2FIT00GTjj4lM7wWJpZ5npbJShyc5lmGp6UwFhdF%2FiJOe8xT8amreI6VgS%2FTOFVHvyWzctGMBpa%2FHf%2BIk%2FmCPRl5YfPLMmaT6ZusF%2FEsfwFD9tiwR0Wel83ZcjPCaUU8RpfmvknLr3xjBc7KLjfMfbT%2BuXpdfPyMnIH7tz14nGcf6CrPcfpEX9iITCMcVMfhuD5GRoSMoB4fuvVxUI8gMB7VR7MemZD16kunPgbsJ3K06wkmGBmBI6NT%2BcqIX%2BINebXholymZACR0zhN5hk5n5KXxgUZeMZFmRB2DegPy2Q2q24fFnid%2FIwf6qVMcr3Kk6yshcEdGm5UrfVU5utG4Kql12WR%2F8CjPM3JulGWZ9Uqj0maykN5VlI5tUJyTSlI9oE3raxBnOEEKThf4rJ4JVM2DBTNHRQj9OplK2%2B2S4mzALLGxmIq4nO%2B7lYKyAkVhAOEwlUYgWcEFPQyL8pFPs%2BzOB1vR4dF%2FpTN8IwSezvnU56vKIH%2FxWX5SilX0V7kbPPM6kG7iUj2lT8VU7xj%2F5ae2AVO4zJ5FtfXEY%2Feel9JzJZJjmkKXOIqii1RxsUcl%2FQuiQV8G8dzxdJCdQCBOQTnOqxRYCKG7hq%2FMq9FTr4skhJ%2FWcU1wV%2BIjtdx7STh53SkdEWBqcg%2FsjTy7%2FUl%2F7ZKaQUQ2WxQWZdKFaXxep1MRbqIROwq2yqNAA12qYATRRs5e0S7gZwi2spCMi8vjRFHb85sIPAmMG1kOgeFxU4GAjr0N5K7vLQyTbPkmZzOq1NgLJvnecA0juvV%2BU%2B%2BYjWt%2Bsh3MwEPs4UdN4vQxxMiwR28C%2Ft5ispgKiLUqAhHgw%2BnLxXh6QWt4eKQCpQgaF34OmwTK1U4ufgMgHC6ikvGxdUUH6kAobn9RsWqxcJfX8z8W7NEhL53vidwwTaPNkbKWgqnerZHgcK%2Fwf2fzBRABTEAnlvUogVOd%2FVolNU7yHVOo04OT0Ir8k29nABJDTWSavcF1vDWwGqj8Gxg1ax1abAyX1WDVo7QYY2kBk%2B%2BBqefVzj7huNyQQBy28bUkuDJkxzQmJqXNKZIk%2Bw6DaCEFMXrP9XFnYN8NvAd%2FhpthKtXeHWPi4S8WsXjd4F3maU8Kj%2FYMvvmnWmH238i8HkG4FLAV1MrH79%2BvWfI94FhnYiuM0%2BDVp57vKzsXPawXtW81HvyDlAjPFMKo4IhCxNrDQO9AppNVVOsJpgQsQiEHFv9ef3Wxh2ClF1RgroqHXoo5JEb1YlISvR6GpWow6%2Ffm0rUpLqqONYBggdDzpEiHz4QS08noipiPBCrInb8nf%2FfioWj8WQvWwFAmkTar%2B3LyrbNlml7gG27rhfraiBNMOaIeSJyDAGkYUpoUG02yedFvHwfiDyHt2qKELSdQFXN9iWjSR3i%2Bq%2FCbT1awZu9c%2Ff4s13h3aF6h6gz2OBkF4VaWNpZE5zGnxbTabUnf3dnX812v4wW6tqcxRGwxGPweJhmcsH8SUc3rGLnp%2FgBp%2F0hvhW6tJ%2BD3mzwLgooUTtw0wr0DyTyMFlTCgU7K60ea0LYlPzxcY37Ueot9QboXAWA87wQIPVpQFmIwHHMPHsT%2BGNjcGwWCXXxCL9RFVVt9pE9woLbjsStNi%2FFy2UD0b0EFkwW2WsXr11Xdd0uW7xGmprBHr10Ho3SKfxVgwkYvPIqGCHOZE0MQHnjAaMlSZenkS6dV9JfDk2taPzigQEPyBkP%2FPDODY6MDWRtoVmr5%2FDAVqPs23AreffoXrcyvKZbabd0ZO7I9IkG%2BLAcXmujgfZ5QHWftaHgXTqatqmXE%2BBoIktKbL91P9Nqkb6DEtRQHveGPFq%2F8SwOyZU9QycUdb2ns90X9Qytm0vquZLt9uVEelfDrSwkV7767v3VJfVMY4CUzg8kwkLqRhPbxCzzkDLX2yhoHWfmbjR8cNrkH8DPumgN3tIkMk7TQaAGz73JLhX47q7l0YnI6yg579gWHNcJ7zzRYXHl9Hbfeq4lecGLhSbrfAvO5ytom7nlfMZWIbmKhjTBQwJlI5GosXgeBhkheyH6%2FPUqzgQoeP895XUBPZ7%2BmNdi%2F2HaKImqRpNkSZnEabNbOrPD%2FqG2h1bhOP9t1Jb5qTI49fvsbjqQvkWBWT%2FIKUfJGzGLIxo0MA2x1eAHbFL4crrwjHd3Q9yq4ZETV46tGh5dJ3V%2F3%2FRc5aO2t5D3CDtaMdvRs%2FRCeY%2F2CgcHOCxejxRPUsqH%2FBIpBncnyuoMg1i3Zt9uvuEUg6ZNmoYy3BC4inGNFHZLhursgYP0Vdi55PDSaQg%2FkEKA639daZ07BOiqLa%2FloQfS55XhsZ9XygsFF%2B4tstt7HrjIw9bB4T7UTgBqR8yh435WcIam2oMQu6tn9kY8N993JVlVPbfLlhxZs8a7%2FXMEJztWLYVJa59a6VsbtHxtDfs9xHaUA9pCdtvn5jxUrPS5qlZXNtrIlBX99a22pvBfMVuN3yXWtiVKtPF7B3V%2FSnvSecL9jnvc75hyYxQYB7unrUmXDh96nB0uvzMgKoQtB%2B2HsK%2BB8BEfe5DL7d%2BRatT79q9x2eP%2FAQ%3D%3D%3C%2Fdiagram%3E%3C%2Fmxfile%3E)

## Требования

Для запуска проекта необходимо установить следующие зависимости:

- `requests` — для выполнения HTTP-запросов к API OpenWeatherMap.
- `aiogram` — библиотека для работы с Telegram Bot API.

Вы можете установить их, выполнив команду:

```bash
pip install requests aiogram
```

## Настройка

1. **Получите токен для Telegram-бота:**
   - Перейдите в Telegram и найдите [BotFather](https://core.telegram.org/bots#botfather).
   - Создайте нового бота и получите токен.
   - Вставьте полученный токен в файл `config.py` в переменную `tg_bot_token`.

2. **Получите токен для OpenWeatherMap API:**
   - Зарегистрируйтесь на [OpenWeatherMap](https://openweathermap.org/).
   - Получите API ключ для доступа к погодным данным.
   - Вставьте API ключ в файл `config.py` в переменную `open_weather_token`.

## Запуск

1. Убедитесь, что у вас установлены все зависимости.
2. Настройте файл `config.py` с вашими токенами.
3. Запустите бота, запустив файл `handlers.py`:

```bash
python handlers.py
```

После этого бот будет работать и слушать входящие сообщения. Вы можете отправить название города, и бот предоставит актуальную информацию о погоде.

## Как пользоваться

1. Напишите боту любое название города.
2. Бот ответит текущей сводкой о погоде в этом городе, включая:
   - Температура
   - Влажность
   - Давление
   - Ветер
   - Время восхода и заката солнца
   - Продолжительность дня

## Пример использования

### Сообщение от пользователя:
```
Москва
```

### Ответ от бота:
```
---2024-11-07 12:34---

Погода в городе: Moscow
Температура: 5°C Ясно ☀️
Влажность: 78%
Давление: 1015 мм.рт.ст
Ветер: 3 м/с
Восход солнца: 07:42:00
Закат солнца: 16:15:00
Продолжительность дня: 8:33:00

---Хорошего дня!---
```

## Логика работы

- Когда пользователь отправляет команду `/start`, бот приветствует его и объясняет, что нужно отправить название города для получения прогноза погоды.
- Когда бот получает сообщение с названием города, он делает запрос к OpenWeatherMap API для получения информации о текущей погоде.
- После получения данных о погоде, бот отправляет сводку пользователю, включая температуру, описание погоды, влажность, давление, скорость ветра и время восхода/заката солнца.
- Если бот не может найти данные о городе, он отправляет ошибку с просьбой проверить правильность названия города.

## Возможные ошибки

- Если бот не может найти информацию о городе (например, неверно указанное название), он отобразит сообщение:
  ```
  ⚠️ Проверьте название города ⚠️
  ```
