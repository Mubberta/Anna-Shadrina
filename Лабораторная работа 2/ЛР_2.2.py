salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
total_spend = 0 #Хранение общей суммы
for month in range(months):
    total_spend += spend
    spend *= (1 + increase)
safety_cushion = total_spend - (salary * months)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(safety_cushion))
