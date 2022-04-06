"""
Отлично! Немного доработать и будет супер!
"""
# Думаю, что это будет лишним, удалим это:)
# coding=utf-8

import datetime as dt


class Record:
    """Присвоим переменной date значение None,
    дабы избежать конфликтов с типом переменной."""
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.date = (
            # Кажется, что переносы строк выглядят неэстетично, необходимо исправить.
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        # Давайте не будем использовать имена переменной с заглавной буквы:)
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            if (
                    # Подумайте, как можно сократить строку? Избавимся от "and".
                    (today - record.date).days < 7 and
                    (today - record.date).days >= 0
                    # И уберем скобки.
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    # Комментарий к функции необходимо оформить в виде Docstrings.
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        # Давайте придумаем нормальное имя переменной:)
        x = self.limit - self.get_today_stats()
        if x > 0:
            # Бэкслеши для переносов не применяются, необходимо исправить.
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        # else в этом случае необязательно, можем убрать.
        else:
            # Обойдемся без скобок.
            return ('Хватит есть!')


class CashCalculator(Calculator):
    """
    Комментарии к курсу валют будут лишними, необходимо убрать.
    Все интуитивно понятно.

    Вместо того, чтобы присваивать тип переменной,
    мы можем сократить запись,
    написав значение переменной типа float напрямую: "60.00" (рекомендация)
    """
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.

    """
    Нет необходимости объявлять аргументы USD_RATE и EURO_RATE
    в функции, мы можем наследовать переменные от класса.
    Сделаем это:)
    """
    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            # Кажется, что эта переменная ничего нам не дает. Уберем ее.
            cash_remained == 1.00
            currency_type = 'руб'
        if cash_remained > 0:
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'Денег нет, держись'
            """
            Здесь мы можем использовать else,
            или же вовсе убрать условие,
            просто оставив возврат функции, которая сработает,
            если все вышеперечисленные условия не выполнятся.
            """
        elif cash_remained < 0:
            """
            1. Избавимся от бэкслешов окончательно.
            Применим "f-строку", как сделано выше.
            2. Нужно определиться, нужен ли нам строковый метод ".format"?
            Думаю, что необходимо придерживаться однообразия в коде. Исправим это.
            """
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)

    # Нам эта функция не нужна, удалим ее.
    def get_week_stats(self):
        super().get_week_stats()


"""
Исполняемый код в .py-файлах должен
быть закрыт конструкцией if __name__ == ‘__main__’.
Необходимо добавить.
"""
