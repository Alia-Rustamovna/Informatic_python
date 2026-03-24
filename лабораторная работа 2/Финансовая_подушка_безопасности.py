money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0
budget = money_capital + salary
new_spend = spend
if budget >= new_spend:
    budget -= new_spend
    count += 1
    budget += salary
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while budget >= new_spend:
    new_spend *= (1+increase)
    budget -= new_spend
    count +=1
    budget += salary
print("Количество месяцев, которое можно протянуть без долгов:", count)
