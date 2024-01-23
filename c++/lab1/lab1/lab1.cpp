#include <iostream>
#include <string>
#include <locale.h>

using namespace std;
class PostalAddress {
private:
    string street;
    int houseNumber;
    string city;
    string postalCode;

public:
    PostalAddress(string st, int num, string ct, string pc)
        : street(st), houseNumber(num), city(ct), postalCode(pc) {}

    void setStreet(const string& st) { street = st; }
    void setHouseNumber(int num) { houseNumber = num; }
    void setCity(const string& ct) { city = ct; }
    void setPostalCode(const string& pc) { postalCode = pc; }

    string getStreet() const { return street; }
    int getHouseNumber() const { return houseNumber; }
    string getCity() const { return city; }
    string getPostalCode() const { return postalCode; }

    // Метод для вывода адреса
    void printAddress() const {
        cout << "Адрес: " << street << ", " << houseNumber
            << ", " << city << ", " << postalCode << endl;
    }
};

int main() {
    setlocale(LC_ALL, "Russian");

    PostalAddress addr("Главная улица", 123, "Город N", "123456");

    int choice;
    string tempStr;
    int tempInt;

    while (true) {
        cout << "\nМенеджер Почтовых Адресов\n";
        cout << "1. Показать адрес\n";
        cout << "2. Изменить улицу\n";
        cout << "3. Изменить номер дома\n";
        cout << "4. Изменить город\n";
        cout << "5. Изменить почтовый индекс\n";
        cout << "6. Выход\n";
        cout << "Выберите действие: ";
        cin >> choice;

        switch (choice) {
        case 1:
            addr.printAddress();
            break;
        case 2:
            cout << "Введите новую улицу: ";
            cin >> tempStr;
            addr.setStreet(tempStr);
            break;
        case 3:
            cout << "Введите новый номер дома: ";
            cin >> tempInt;
            addr.setHouseNumber(tempInt);
            break;
        case 4:
            cout << "Введите новый город: ";
            cin >> tempStr;
            addr.setCity(tempStr);
            break;
        case 5:
            cout << "Введите новый почтовый индекс: ";
            cin >> tempStr;
            addr.setPostalCode(tempStr);
            break;
        case 6:
            return 0;
        default:
            cout << "Неверный выбор. Попробуйте снова.\n";
        }
    }

    return 0;
}
