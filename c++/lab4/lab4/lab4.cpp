#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <locale.h>

class AEROFLOT {
private:
    std::string destination;
    int flightNumber;
    std::string planeType;

public:
    AEROFLOT() : destination(""), flightNumber(0), planeType("") {}
    AEROFLOT(std::string dest, int number, std::string type)
        : destination(dest), flightNumber(number), planeType(type) {}

    void setDestination(const std::string& dest) { destination = dest; }
    void setFlightNumber(int number) { flightNumber = number; }
    void setPlaneType(const std::string& type) { planeType = type; }

    std::string getDestination() const { return destination; }
    int getFlightNumber() const { return flightNumber; }
    std::string getPlaneType() const { return planeType; }

    // Перегрузка операторов
    friend std::istream& operator>>(std::istream& in, AEROFLOT& a);
    friend std::ostream& operator<<(std::ostream& out, const AEROFLOT& a);
};

std::istream& operator>>(std::istream& in, AEROFLOT& a) {
    setlocale(LC_ALL, "Russian");
    std::cout << "Пункт назначения: ";
    in >> a.destination;
    std::cout << "Номер рейса: ";
    in >> a.flightNumber;
    std::cout << "Тип самолета: ";
    in >> a.planeType;
    return in;
}

std::ostream& operator<<(std::ostream& out, const AEROFLOT& a) {
    setlocale(LC_ALL, "Russian");
    out << "Номер рейса: " << a.flightNumber << ", Тип самолета: " << a.planeType
        << ", Пункт назначения: " << a.destination;
    return out;
}

bool compareFlightNumber(const AEROFLOT& a1, const AEROFLOT& a2) {
    return a1.getFlightNumber() < a2.getFlightNumber();
}

int main() {
    setlocale(LC_ALL, "Russian");
    std::vector<AEROFLOT> flights(7);
    std::string searchDestination;

    std::cout << "Введите данные о 7 рейсах (пункт назначения, номер рейса, тип самолета):\n";
    for (int i = 0; i < 7; ++i) {
        std::cout << "\n" << i + 1 << " рейс:\n";
        std::cin >> flights[i];
    }

    std::sort(flights.begin(), flights.end(), compareFlightNumber);

    std::cout << "\nВведите пункт назначения для поиска рейсов: ";
    std::cin >> searchDestination;

    bool found = false;
    for (const auto& flight : flights) {
        if (flight.getDestination() == searchDestination) {
            std::cout << flight << std::endl;
            found = true;
        }
    }

    if (!found) {
        std::cout << "Рейсы в " << searchDestination << " не найдены." << std::endl;
    }

    return 0;
}
