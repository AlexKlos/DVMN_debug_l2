import os

from dotenv import load_dotenv

from weather_sdk import get_new_event, SMSServer


load_dotenv()
FORECAST_TOKEN = os.getenv('FORECAST_TOKEN')
town_title = 'Курск'

SMS_TOKEN = os.getenv('SMS_TOKEN')
server = SMSServer(SMS_TOKEN)

new_event = get_new_event(FORECAST_TOKEN, town_title)
event_date = new_event.get_date()
event_time = new_event.get_time()
event_area = new_event.get_area()
phenomenon_description = new_event.get_phenomenon()

sms_template = '''{town_title}: {event_time} {event_date} {event_area} ожидается {phenomenon_description}. Будьте внимательны и осторожны.'''

sms_message = sms_template.format(
    phenomenon_description=phenomenon_description,
    town_title=town_title,
    event_time=event_time,
    event_date=event_date,
    event_area=event_area,
)

server.send(sms_message)


# Гипотеза 1: В переменной нет прогноза погоды для Курска
# Способ проверки: Выведу переменную new_event
# Код для проверки: print('new_event:', new_event)
# Установленный факт: new_event: Регион:  Погода:
# Вывод: Гипотеза верна - переменная new_event пустая

# Гипотеза 2.1: town_title на самом деле пуста
# Способ проверки: Вывести переменную town_title
# Код для проверки: print('town_title:', town_title)
# Установленный факт: town_title: Курск
# Вывод: Гипотеза не подтвердилась - в переменной town_title название города

# Гипотеза 2.2: В town_title не название города
# Способ проверки: Вывести переменную town_title
# Код для проверки: print('town_title:', town_title)
# Установленный факт: town_title: Курск
# Вывод: Гипотеза не подтвердилась - в переменной town_title название города

# Гипотеза 3: Переменная token на самом деле пуста
# Способ проверки: Вывести переменную token
# Код для проверки: print('token:', token)
# Установленный факт: token: None
# Вывод: Гипотеза подтверждена - переменная token не определена

# Гипотеза 4.1: Может, `token` всё ещё пуст?
# Способ проверки: Вывести переменную token
# Код для проверки: print('token:', token)
# Установленный факт: token: None
# Вывод: Гипотеза подтверждена - token пуст

# Гипотеза 4.2: Может, в токене не то значение, не `85b98d96709fd49a69ba8165676e4592`?
# Способ проверки: Вывести переменную token
# Код для проверки: print('token:', token)
# Установленный факт: token: None
# Вывод: Гипотеза не подтверждена - пуст

# Гипотеза 4.3: Может, значение `85b98d96709fd49a69ba8165676e4592` успевает измениться до строчки `new_event = ...`?
# Способ проверки: Вывести переменную token сразу после инициализации
# Код для проверки: print('token:', token)
# Установленный факт: token: None
# Вывод: Гипотеза не подтверждена - token пуст

# Гипотеза 5.1: Переменная `event_time` пуста/в ней не время
# Способ проверки: Вывести переменную event_time
# Код для проверки: print('event_time:', event_time)
# Установленный факт: event_time: в вечернее и ночное время
# Вывод: Гипотеза не подтверждена

# Гипотеза 5.2: Переменная `event_date` пуста/в ней не дата
# Способ проверки: Вывести переменную event_date
# Код для проверки: print('event_date:', event_date)
# Установленный факт: event_date: 22 ноября
# Вывод: Гипотеза не подтверждена

# Гипотеза 5.3: Переменная `event_area` пуста/в ней не место
# Способ проверки: Вывести переменную event_area
# Код для проверки: print('event_area:', event_area)
# Установленный факт: event_area: к. Тамбей
# Вывод: Гипотеза не подтверждена

# Гипотеза 5.4: Переменная `phenomenon_description` пуста/в ней не описание погодного явления
# Способ проверки: Вывести переменную phenomenon_description
# Код для проверки: print('phenomenon_description:', phenomenon_description)
# Установленный факт: phenomenon_description: ледяной дождь
# Вывод: Гипотеза не подтверждена

# Гипотеза 6: Возможно, в шаблоне используются какие-то переменные, которые не передаются в .format()
# Способ проверки: Заменить переменные в шаблоне на корректные
# Код для проверки: ...
# Установленный факт: Та же ошибка - ' sms_message = sms_template.format(' ... 'KeyError: 'town_title''
# Вывод: Гипотеза не подтвержена

# Гипотеза 7: Возможно дело в фигурных скобках в шаблоне?
# Способ проверки: Вывести шаблон с форматированием
# Код для проверки: print('{town_title}: {event_time} {event_date} {event_area} ожидается {phenomenon_description}. Будьте внимательны и осторожны.'.format(phenomenon_description=phenomenon_description, town_title=town_title, event_time=event_time, event_date=event_date, event_area=event_area))
# Установленный факт: Курск: вечером 25 ноября к. Карталы ожидается ледяной дождь. Будьте внимательны и осторожны.
# Вывод: Гипотеза не подтвердилась - шаблон в порядке

# Гипотеза 8: При форматировании строки, именованные аргументы передаются в формате: имя=значение
# Способ проверки: изменить формат агрументов
# Код для проверки: sms_message = sms_template.format(
#                       phenomenon_description=phenomenon_description,
#                       town_title=town_title,
#                       event_time=event_time,
#                       event_date=event_date,
#                       event_area=event_area,
#                   )
# Установленный факт: Рассылаю сообщение:
#                      Курск: в вечернее и ночное время 23 ноября п. Серафимович ожидается заморозки до минус 35 градусов. Будьте внимательны и осторожны.
#                      |█ |█████████████████████████████░| 100.0%
# Вывод: Гипотеза верна
