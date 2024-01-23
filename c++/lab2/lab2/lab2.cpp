#include <iostream>
#include <string>
#include <sstream>
#include <map>

class SymbString {
private:
    std::string id;
    std::string value;

public:
    SymbString(const std::string& id, const std::string& value) : id(id), value(value) {}

    void showValue() const {
        std::cout << "ID: " << id << " | Value: " << value << std::endl;
    }

    std::string getId() const {
        return id;
    }

    std::string getValue() const {
        return value;
    }

    int toDecimal() const {
        return std::stoi(value); //строка в десятичное число
    }
};

class OctString {
private:
    std::string id;
    std::string value;

public:
    OctString(const std::string& id, const std::string& value) : id(id), value(value) {}

    void showValue() const {
        std::cout << "ID: " << id << " | Value: " << value << std::endl;
    }

    std::string getId() const {
        return id;
    }

    int toDecimal() const {
        int decimalValue;
        std::stringstream ss;
        ss << std::oct << value;
        ss >> decimalValue;
        return decimalValue; // восьмеричное в десятичное
    }
};

// + между SymbString и OctString
SymbString operator+(const SymbString& symb, const OctString& oct) {
    int symbAsDecimal = symb.toDecimal();
    int octAsDecimal = oct.toDecimal();
    int sum = symbAsDecimal + octAsDecimal; // сложение в десятичной форме
    return SymbString(symb.getId() + "+" + oct.getId(), std::to_string(sum)); //сумма как строка
}

class Factory {
private:
    std::map<std::string, SymbString*> symbStrings;
    std::map<std::string, OctString*> octStrings;

public:
    ~Factory() {
        for (auto& pair : symbStrings) {
            delete pair.second;
        }
        for (auto& pair : octStrings) {
            delete pair.second;
        }
    }

    SymbString* createSymbString(const std::string& id, const std::string& value) {
        SymbString* newObj = new SymbString(id, value);
        symbStrings[id] = newObj;
        return newObj;
    }

    OctString* createOctString(const std::string& id, const std::string& value) {
        OctString* newObj = new OctString(id, value);
        octStrings[id] = newObj;
        return newObj;
    }

    void deleteSymbString(const std::string& id) {
        auto it = symbStrings.find(id);
        if (it != symbStrings.end()) {
            delete it->second;
            symbStrings.erase(it);
        }
    }

    void deleteOctString(const std::string& id) {
        auto it = octStrings.find(id);
        if (it != octStrings.end()) {
            delete it->second;
            octStrings.erase(it);
        }
    }

    void showAll() {
        for (const auto& pair : symbStrings) {
            pair.second->showValue();
        }
        for (const auto& pair : octStrings) {
            pair.second->showValue();
        }
    }
};

int main() {
    Factory factory;
    SymbString* s1 = factory.createSymbString("S1", "123"); // Десятичное число в виде строки
    OctString* o1 = factory.createOctString("O1", "10");   // Восьмеричное число, равное 8 в десятичной системе

    s1->showValue();
    o1->showValue();

    SymbString result = *s1 + *o1;
    result.showValue(); //Сумма в десятичной форме

    factory.deleteSymbString(s1->getId());
    factory.deleteOctString(o1->getId());

    return 0;
}
