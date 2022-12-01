# Task number 1
def task_01_money(rubles: int, coins: int, amount: int) -> float:
    float_price = float(rubles + (coins / 100))
    print(float_price * amount)
    return (float_price * amount)


task_01_money(11, 4, 4)
