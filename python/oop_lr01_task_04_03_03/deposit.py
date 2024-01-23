class TimeDeposit:
    def __init__(self, name, interest_rate, period_limit, sum_limit):
        self.name = name
        self._interest_rate = interest_rate
        self._period_limit = period_limit
        self._sum_limit = sum_limit
        self._check_self()

    def __str__(self):
        return f"""
Наименование:       {self.name}
Валюта:             {self.currency}
Процентная ставка:  {self._interest_rate}
Срок (мес.):        {self._period_limit}
Сумма:              {self._sum_limit}
"""

    @property
    def currency(self):
        return "руб."

    def _check_self(self):
        assert 0 < self._interest_rate <= 100
        assert 1 <= self._period_limit[0] < self._period_limit[1]
        assert 0 < self._sum_limit[0] <= self._sum_limit[1]

    def check_user_params(self, initial_sum, period):
        is_sum_ok = self._sum_limit[0] <= initial_sum < self._sum_limit[1]
        is_period_ok = self._period_limit[0] <= period < self._period_limit[1]
        assert is_sum_ok and is_period_ok, "Условия вклада не соблюдены!"

    def get_profit(self, initial_sum, period):
        self.check_user_params(initial_sum, period)
        return initial_sum * self._interest_rate / 100 * period / 12

    def get_sum(self, initial_sum, period):
        return initial_sum + self.get_profit(initial_sum, period)


class BonusTimeDeposit(TimeDeposit):
    def __init__(self, name, interest_rate, period_limit, sum_limit, bonus):
        super().__init__(name, interest_rate, period_limit, sum_limit)
        self._bonus = bonus

    def __str__(self):
        return super().__str__() + f"\nБонус (%):          {self._bonus['percent']}" \
                                     f"\nБонус (мин. сумма): {self._bonus['sum']}"

    def check_self(self):
        super()._check_self()
        assert 0 < self._bonus["percent"] <= 100
        assert self._bonus["sum"] > 0
        assert self._bonus["sum"] <= self._sum_limit[1]

    def get_profit(self, initial_sum, period):
        profit = super().get_profit(initial_sum, period)
        if initial_sum >= self._bonus["sum"]:
            profit += profit * self._bonus["percent"] / 100
        return profit


class CompoundTimeDeposit(TimeDeposit):
    def __str__(self):
        return super().__str__() + "\nКапитализация %: Да"

    def get_profit(self, initial_sum, period):
        self.check_user_params(initial_sum, period)
        rate = 1 + self._interest_rate / 100 / 12
        return initial_sum * (rate ** period) - initial_sum
