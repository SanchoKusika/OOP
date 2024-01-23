#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include <locale.h>

bool isVowel(char ch) {
    ch = tolower(ch);
    return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
}

int main() {
    setlocale(LC_ALL, "Russian");
    std::ifstream file("words.txt");
    std::vector<std::string> words;
    std::string word;

    if (!file.is_open()) {
        std::cerr << "Ошибка при открытии файла" << std::endl;
        return 1;
    }

    while (file >> word) {
        words.push_back(word);
    }

    file.close();

    // Вывод всех слов
    std::cout << "Все слова:" << std::endl;
    for (const auto& w : words) {
        std::cout << w << std::endl;
    }

    // Вывод слов, начинающихся с гласных
    std::cout << "\nСлова, начинающиеся с гласной:" << std::endl;
    for (const auto& w : words) {
        if (isVowel(w[0])) {
            std::cout << w << std::endl;
        }
    }

    return 0;
}
