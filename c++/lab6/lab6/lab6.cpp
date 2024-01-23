#include <iostream>
#include <list>
#include <string>
#include <locale.h>

struct Bus {
    int busNumber;
    std::string driverName;
    int routeNumber;
};

void printBuses(const std::list<Bus>& buses) {
    setlocale(LC_ALL, "Russian");
    if (buses.empty()) {
        std::cout << "Автобусов для отображения нет." << std::endl;
        return;
    }
    for (const auto& bus : buses) {
        std::cout << "Номер автобуса: " << bus.busNumber << ", Водитель: " << bus.driverName << ", Маршрут: " << bus.routeNumber << "\n";
    }
}

void transferBus(std::list<Bus>& from, std::list<Bus>& to, int busNumber) {
    setlocale(LC_ALL, "Russian");
    for (auto it = from.begin(); it != from.end(); ++it) {
        if (it->busNumber == busNumber) {
            to.push_back(*it);
            from.erase(it);
            return;
        }
    }
    std::cout << "Автобус с номером " << busNumber << " не найден." << std::endl;
}

int main() {
    setlocale(LC_ALL, "Russian");
    std::list<Bus> busesInPark;
    std::list<Bus> busesOnRoute;
    int choice, busNumber;
    std::string driverName;
    int routeNumber;

    while (true) {
        std::cout << "\n1. Добавить автобус в парк\n"
            << "2. Отправить автобус на маршрут\n"
            << "3. Вернуть автобус в парк\n"
            << "4. Показать автобусы в парке\n"
            << "5. Показать автобусы на маршруте\n"
            << "6. Выйти\n"
            << "Введите ваш выбор: ";
        std::cin >> choice;

        switch (choice) {
        case 1:
            std::cout << "\nНомер автобуса: ";
            std::cin >> busNumber;
            std::cout << "Водитель: ";
            std::cin >> driverName;
            std::cout << "Маршрут: ";
            std::cin >> routeNumber;
            busesInPark.push_back({ busNumber, driverName, routeNumber });
            break;
        case 2:
            std::cout << "\nВведите номер автобуса для отправки на маршрут: ";
            std::cin >> busNumber;
            transferBus(busesInPark, busesOnRoute, busNumber);
            break;
        case 3:
            std::cout << "\nВведите номер автобуса для возвращения в парк: ";
            std::cin >> busNumber;
            transferBus(busesOnRoute, busesInPark, busNumber);
            break;
        case 4:
            std::cout << "\nАвтобусы в парке:\n";
            printBuses(busesInPark);
            break;
        case 5:
            std::cout << "\nАвтобусы на маршрутах:\n";
            printBuses(busesOnRoute);
            break;
        case 6:
            return 0;
        default:
            std::cout << "\nНеверный выбор. Попробуйте еще раз.\n";
        }
    }

    return 0;
}
