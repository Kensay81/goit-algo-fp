def greedy_algorithm(items, budget):
    item_list = [(name, details["cost"], details["calories"]) for name, details in items.items()]
    item_list.sort(key=lambda x: x[2] / x[1], reverse=True)
    
    total_cost = 0
    total_calories = 0
    chosen_items = []
    
    for name, cost, calories in item_list:
        if total_cost + cost <= budget:
            chosen_items.append(name)
            total_cost += cost
            total_calories += calories
    
    return chosen_items, total_calories, total_cost


def dynamic_programming(items, budget):
    item_list = [(name, details["cost"], details["calories"]) for name, details in items.items()]
    n = len(item_list)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name, cost, calories = item_list[i-1]
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost] + calories)
            else:
                dp[i][w] = dp[i-1][w]
    
    w = budget
    chosen_items = []
    total_calories = dp[n][w]
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            name, cost, calories = item_list[i-1]
            chosen_items.append(name)
            w -= cost
    
    return chosen_items, total_calories, budget - w

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
chosen_items, total_calories, total_cost = greedy_algorithm(items, budget)
print("Результат роботи жадібного алгоритму:")
print(f"Обрані страви : {chosen_items}")
print(f"Всього калорій : {total_calories}")
print(f"Загальна вартість : {total_cost}\n")


chosen_items, total_calories, total_cost = dynamic_programming(items, budget)
print("Результат роботи функції динамічного програмування:")
print(f"Обрані страви : {chosen_items}")
print(f"Всього калорій : {total_calories}")
print(f"Загальна вартість : {total_cost}")