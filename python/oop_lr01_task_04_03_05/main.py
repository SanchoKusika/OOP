from time_class import Time, TimeCollection


# Пример использования
if __name__ == "__main__":
    collection = TimeCollection()
    collection.add(Time(2, 45, 30))
    collection.add(Time.from_string("03:15:45"))

    print("Коллекция времени:")
    print(collection)

    # Сохранение коллекции в файл
    collection.save("times_collection.json")

    # Загрузка коллекции из файла
    new_collection = TimeCollection()
    new_collection.load("times_collection.json")
    print("\nЗагруженная коллекция времени:")
    print(new_collection)
