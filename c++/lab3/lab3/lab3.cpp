#include <iostream>
#include <stdexcept>
#include <locale.h>


template <typename T>
class Vect {
public:
    T* data;
    size_t size;
    size_t capacity;

    void resize(size_t new_capacity) {
        T* temp = new T[new_capacity];
        for (size_t i = 0; i < size; ++i) {
            temp[i] = data[i];
        }
        delete[] data;
        data = temp;
        capacity = new_capacity;
    }

public:
    Vect() : data(nullptr), size(0), capacity(0) {}

    ~Vect() {
        delete[] data;
    }

    void push_back(const T& value) {
        if (size == capacity) {
            resize(capacity == 0 ? 1 : capacity * 2);
        }
        data[size++] = value;
    }

    T& operator[](size_t index) {
        setlocale(LC_ALL, "Russian");
        if (index >= size) {
            throw std::out_of_range("Индекс выходит за границы массива");
        }
        return data[index];
    }

    // Константная перегрузка оператора []
    const T& operator[](size_t index) const {
        setlocale(LC_ALL, "Russian");
        if (index >= size) {
            throw std::out_of_range("Индекс выходит за границы массива");
        }
        return data[index];
    }

    size_t getSize() const {
        return size;
    }

    void print() const {
        if (size == 0) {
            std::cout << "[]";
        }
        else {
            for (size_t i = 0; i < size; ++i) {
                std::cout << "[" << data[i] << "] ";
            }
        }
        std::cout << std::endl;
    }

    void pop_back() {
        if (size == 0) {
            throw std::out_of_range("Попытка удалить элемент из пустого массива");
        }
        size--;
    }
};


template <typename T>
class Stack {
private:
    Vect<T> vect;

public:
    void push(const T& value) {
        vect.push_back(value);
    }

    T pop() {
        if (vect.getSize() == 0) {
            setlocale(LC_ALL, "Russian");
            throw std::underflow_error("Стек пуст");
        }
        T value = vect[vect.getSize() - 1];
        vect.pop_back();
        return value;
    }

    T top() const {
        if (vect.getSize() == 0) {
            setlocale(LC_ALL, "Russian");
            throw std::underflow_error("Стек пуст");
        }
        return vect[vect.getSize() - 1];
    }

    bool isEmpty() const {
        return vect.getSize() == 0;
    }

    void print() const {
        vect.print();
    }

};

int main() {
    setlocale(LC_ALL, "Russian");
    try {
        Stack<int> intStack;

        intStack.push(10);
        intStack.push(20);
        intStack.push(30);

        std::cout << "Содержимое стека до изменений: ";
        intStack.print();

        std::cout << "Удаленный элемент: " << intStack.pop() << std::endl;
        std::cout << "Удаленный элемент: " << intStack.pop() << std::endl;
        std::cout << "Удаленный элемент: " << intStack.pop() << std::endl;
        
        std::cout << "Содержимое стека после изменений: ";
        intStack.print();

        intStack.pop();
    }

    catch (const std::exception& e) {
        std::cerr << "Исключение: " << e.what() << std::endl;
    }

    return 0;
}
