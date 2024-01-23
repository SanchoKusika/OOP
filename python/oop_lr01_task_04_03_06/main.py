from переводы import ДенежныйПеревод, ПочтовыйПеревод, БанковскийПеревод, ВалютныйПеревод

if __name__ == "__main__":
    денежный = ДенежныйПеревод(1000, "Иван", "Петр")
    почтовый = ПочтовыйПеревод(500, "Алексей", "Мария", "г. Москва")
    банковский = БанковскийПеревод(2000, "Ольга", "Николай", "123456789")
    валютный = ВалютныйПеревод(300, "Дмитрий", "Елена", "USD")

    for перевод in [денежный, почтовый, банковский, валютный]:
        print(перевод)
        print(перевод.выполнить())