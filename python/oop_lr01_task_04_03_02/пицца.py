# Программирование на языке высокого уровня (Python).
# Задание №2.
#
# Выполнил: Кузнецов Александр Павлович.
# Группа: ПИН-б-о-21-1
# E-mail: sanchezzkusika@gmail.com


# пицца.py

class Пицца:

    def __init__(self):
        self.название = "Заготовка"
        self.тесто = "тонкое"
        self.соус = "кечтуп"
        self.начинка = []
        self.цена = 0

    def __str__(self):
        return (
            f"Пицца: {self.название} | Цена: {self.цена:.2f} р.\n"
            f"Тесто: {self.тесто} Соус: {self.соус}\n"
            f"Начинка: {', '.join(self.начинка)}"
        )

    def подготовить(self):
        print(f"Начинаю готовить пиццу {self.название}")
        print(f"  - замешиваю {self.тесто} тесто...")
        print(f"  - добавляю соус: {self.соус}...")
        print(f"  - и, конечно: {', '.join(self.начинка)}...")

    def испечь(self):
        print("Выпекаю пиццу... Готово!")

    def нарезать(self):
        print("Нарезаю на аппетитные кусочки...")

    def упаковать(self):
        print("Упаковываю в фирменную упаковку и готово!")


class ПиццаПепперони(Пицца):

    def __init__(self):
        super().__init__()
        self.название = "Пепперони"
        self.цена = 350
        self.соус = "томатный"
        self.начинка = ["пепперони", "сыр моцарелла"]


class ПиццаБарбекю(Пицца):

    def __init__(self):
        super().__init__()
        self.название = "Барбекю"
        self.цена = 450
        self.соус = "барбекю"
        self.начинка = ["бекон", "ветчина", "зелень", "сыр моцарелла"]


class ПиццаДарыМоря(Пицца):

    def __init__(self):
        super().__init__()
        self.название = "Дары моря"
        self.цена = 550
        self.тесто = "пышное"
        self.соус = "тар-тар"
        self.начинка = ["кальмары", "креветки", "мидии", "сыр моцарелла"]
