from deposits import deposits


if __name__ == "__main__":
    print("\nДобро пожаловать в систему подбора вкладов!")

    while True:
        print("\n-----")
        print("Нажмите 1, чтобы подобрать вклад, или что угодно для выхода.")

        answer = input()
        if answer == "1":
            try:
                initial_sum = float(input("1/2: Введите начальную сумму вклада: "))
                period = int(input("2/2: Введите срок вклада (мес.): "))
            except ValueError:
                print("Ошибка ввода. Введите корректные числовые значения.")
                continue

            matched_deposits = []
            for deposit in deposits:
                try:
                    deposit.check_user_params(initial_sum, period)
                    matched_deposits.append(deposit)
                except AssertionError as err:
                    pass

            if len(matched_deposits) > 0:
                print("{0:18} | {1:13} | {2:13}".format(
                    "Вклад", "Прибыль", "Итоговая сумма"
                ))
                for deposit in matched_deposits:
                    print("{0:18} | {1:8,.2f} {3:4} | {2:8,.2f} {3:4}".format(
                        deposit.name,
                        deposit.get_profit(initial_sum, period),
                        deposit.get_sum(initial_sum, period),
                        deposit.currency))
            else:
                print("К сожалению, нет подходящих Вам вкладов.")
        else:
            break

    print("\nСпасибо, что воспользовались терминалом банка! До встречи!")

# -------------
# Пример вывода (файл):
#
# Добро пожаловать в систему подбора вкладов!
#
# -----
# Нажмите 1, чтобы подобрать вклад, или что угодно для выхода.
# 1
# 1/2: Введите начальную сумму вклада: 1000
# 2/2: Введите срок вклада (мес.): 12
# Вклад              | Прибыль       | Итоговая сумма
# Сохраняй           |    50.00 руб. | 1,050.00 руб.
# Бонусный           |    50.00 руб. | 1,050.00 руб.
# С капитализацией   |    51.16 руб. | 1,051.16 руб.
