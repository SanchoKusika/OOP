from time_class import Time


if __name__ == "__main__":
    time1 = Time(2, 45, 30)
    time2 = Time.from_string("03:15:45")

    print(f"Время 1: {time1}")
    print(f"Время 2: {time2}")

    # Тестирование сложения и вычитания
    print(f"Сумма: {time1 + time2}")
    print(f"Разница: {time1 - time2}")

    # Сохранение и загрузка из JSON
    time1.save("time1.json")
    loaded_time = Time.load("time1.json")
    print(f"Загруженное Время(Time): {loaded_time}")
