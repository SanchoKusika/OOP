
class Roman:

    # Константы класса
    ARABIC_MIN = 1
    ARABIC_MAX = 3999
    ROMAN_MIN = "I"
    ROMAN_MAX = "MMMCMXCIX"

    LETTERS = ["M", "CM", "D", "CD", "C", "XC", "L",
               "XL", "X", "IX", "V", "IV", "I"]
    NUMBERS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    def __init__(self, value):
        """Инициализация класса.

        Параметры:
            value (str): римское число, например, X.
                или
            value (int): арабское число, например, 5.
                или
            value (другой тип):  возбудить исключение TypeError.
        """
        if not isinstance(value, (int, str)):
            raise TypeError("Не могу создать римское число из {0}".
                            format(type(value)))

        if isinstance(value, int):
            self._arabic = value
        elif isinstance(value, str):
            self._arabic = self.to_arabic(value)
            self._roman = value

        if self._arabic < Roman.ARABIC_MIN or self._arabic > Roman.ARABIC_MAX:
            raise ValueError(f"Значение {value} вне диапазона [{Roman.ARABIC_MIN}; {Roman.ARABIC_MAX}]")

    def __add__(self, other):
        if isinstance(other, Roman):
            result_arabic = self._arabic + other._arabic
        elif isinstance(other, int):
            result_arabic = self._arabic + other
        else:
            raise TypeError(f"Нельзя сложить римское число с {type(other)}")

        return Roman(result_arabic)

    def __sub__(self, other):
        if isinstance(other, Roman):
            result_arabic = self._arabic - other._arabic
        elif isinstance(other, int):
            result_arabic = self._arabic - other
        else:
            raise TypeError(f"Нельзя вычесть римское число из {type(other)}")

        return Roman(result_arabic)

    def __mul__(self, other):
        if isinstance(other, Roman):
            result_arabic = self._arabic * other._arabic
        elif isinstance(other, int):
            result_arabic = self._arabic * other
        else:
            raise TypeError(f"Нельзя умножить римское число на {type(other)}")

        return Roman(result_arabic)

    def __floordiv__(self, other):
        if isinstance(other, Roman):
            result_arabic = self._arabic // other._arabic
        elif isinstance(other, int):
            result_arabic = self._arabic // other
        else:
            raise TypeError(f"Нельзя делить римское число на {type(other)}")

        return Roman(result_arabic)

    def __truediv__(self, other):
        """Создать новый объект как частное self и other.

        Параметры:
            other (Roman): ...
                или
            other (int): арабское число, добавить к self.
                или
            other (другой тип):  возбудить исключение TypeError.
        """
        # Любое деление для римского числа считается делением нацело,
        # поэтому необходимо передать "работу" реализованному методу
        # целочисленного деления
        if isinstance(other, Roman):
            result_arabic = self._arabic / other._arabic  # Обычное деление, возвращает float
        elif isinstance(other, int):
            result_arabic = self._arabic / other  # Обычное деление, возвращает float
        else:
            raise TypeError(f"Нельзя делить римское число на {type(other)}")

        return Roman(int(result_arabic))  # Преобразуем результат в целое число и создаем новый объект Roman

    def __str__(self):
        """Вернуть строковое представление класса."""
        return self.to_roman(self.arabic)

    @staticmethod
    def __check_arabic(value):
        """Возбудить исключение ValueError, если 'value' не принадлежит
        [ARABIC_MIN; ARABIC_MIN]."""
        if not Roman.ARABIC_MIN <= value <= Roman.ARABIC_MAX:
            raise ValueError(f"Значение {value} вне диапазона [{Roman.ARABIC_MIN}; {Roman.ARABIC_MAX}]")

    @staticmethod
    def __check_roman(value):
        """Возбудить исключение ValueError, если 'value' содержит
        недопустимые символы (не входящие в LETTERS)."""
        for letter in value:
            if letter not in Roman.LETTERS:
                raise ValueError(f"Недопустимый символ в римском числе: {letter}")

    @property
    def arabic(self):
        """Вернуть арабское представление числа."""
        return self._arabic

    @staticmethod
    def to_arabic(roman):
        """Преобразовать римское число 'roman' в арабское.

        Параметры:
            roman (str): римское число, например, "X".

        Возвращает:
            int: арабское число.
        """

        def letter_to_number(letter):
            """Вернуть арабское значение римской цифры 'letter'.

            Регистр не учитывается."""
            letter = letter.upper()  # Привести к верхнему регистру
            return Roman.NUMBERS[Roman.LETTERS.index(letter)]

        Roman.__check_roman(roman)

        i = 0  # Позиция в строке roman
        value = 0  # Преобразованное число

        while i < len(roman):
            number = letter_to_number(roman[i])
            i += 1

            if i == len(roman):
                # В строке roman больше не осталось символов, добавляем number
                value += number
            else:
                # Если символы остались, необходимо посмотреть на следующий.
                # Если следующий символ "больше", считаем их за одну цифру.
                # Это необходимо, например, для того,
                # чтобы IV преобразовать в 4, а не 15.
                next_number = letter_to_number(roman[i])
                if next_number > number:
                    # Комбинируем цифры и перемещаем i к следующей
                    value += next_number - number
                    i += 1
                else:
                    # Просто добавляем следующую цифру
                    value += number

        Roman.__check_arabic(value)
        return value

    @staticmethod
    def to_roman(arabic):
        Roman.__check_arabic(arabic)

        roman = ""
        # n - часть arabic, которую осталось преобразовать
        n = arabic

        for i, number in enumerate(Roman.NUMBERS):
            while n >= number:
                roman += Roman.LETTERS[i]
                n -= Roman.NUMBERS[i]
        return roman
