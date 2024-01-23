from deposit import TimeDeposit, BonusTimeDeposit, CompoundTimeDeposit

deposits = [
    TimeDeposit(name="Сохраняй", interest_rate=5, period_limit=(6, 18), sum_limit=(1000, 100001)),

    BonusTimeDeposit(name="Бонусный", interest_rate=5, period_limit=(6, 18),
                     sum_limit=(1000, 100001), bonus={"percent": 5, "sum": 2000}),

    CompoundTimeDeposit(name="С капитализацией", interest_rate=5, period_limit=(6, 18), sum_limit=(1000, 100001))
]
