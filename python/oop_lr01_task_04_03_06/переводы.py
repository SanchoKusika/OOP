class Перевод:
    def __init__(self, сумма, отправитель, получатель):
        self.отправитель = отправитель  # общедоступное поле
        self._сумма = сумма  # защищенное поле
        self.__получатель = получатель  # закрытое поле

    def выполнить(self):
        raise NotImplementedError("Метод 'выполнить' должен быть переопределен в подклассе")

    def __str__(self):
        return f"Перевод: {self._сумма} от {self.отправитель} к {self.__получатель}"

class ДенежныйПеревод(Перевод):
    def __init__(self, сумма, отправитель, получатель):
        super().__init__(сумма, отправитель, получатель)
        self.дата = None  # общедоступное поле

    def выполнить(self):
        self.дата = "сегодня"  # пример общедоступного метода
        return f"Денежный перевод на сумму {self._сумма} успешно выполнен."

    def _печатьИнформации(self):  # защищенный метод
        return f"Информация о переводе: {self.__str__()}"

class ПочтовыйПеревод(Перевод):
    def __init__(self, сумма, отправитель, получатель, адрес):
        super().__init__(сумма, отправитель, получатель)
        self._адрес = адрес  # защищенное поле

    def выполнить(self):
        return f"Почтовый перевод на сумму {self._сумма} отправлен по адресу {self._адрес}."

    def получитьАдрес(self):  # общедоступный метод
        return self._адрес

class БанковскийПеревод(Перевод):
    def __init__(self, сумма, отправитель, получатель, номерСчета):
        super().__init__(сумма, отправитель, получатель)
        self.__номерСчета = номерСчета  # закрытое поле

    def выполнить(self):
        return f"Банковский перевод на сумму {self._сумма} зачислен на счет {self.__номерСчета}."

    def _проверитьСчет(self):  # защищенный метод
        return f"Проверка счета: {self.__номерСчета}"

class ВалютныйПеревод(Перевод):
    def __init__(self, сумма, отправитель, получатель, валюта):
        super().__init__(сумма, отправитель, получатель)
        self.валюта = валюта  # общедоступное поле

    def выполнить(self):
        return f"Валютный перевод на сумму {self._сумма} {self.валюта} успешно выполнен."

    def _конвертацияВалюты(self):  # защищенный метод
        return f"Конвертация валюты: {self.валюта}"
