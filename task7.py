import random

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def simulate_rolls(num_rolls):
    sum_counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        die1, die2 = roll_dice()
        dice_sum = die1 + die2
        sum_counts[dice_sum] += 1
    
    probabilities = {k: v / num_rolls for k, v in sum_counts.items()}
    
    return sum_counts, probabilities

num_rolls = 1000000
sum_counts, probabilities = simulate_rolls(num_rolls)

# Аналітичні ймовірності
analytical_probs = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

header = f"{'Сума':<8}{'Метод Монте карло:':<24}{'Аналітичний метод:':<24}"
print(header)
print("-" * len(header))
for sum_ in range(2, 13):
    sim_prob = probabilities.get(sum_, 0)
    analit_prob = analytical_probs.get(sum_, 0)
    print(f"{sum_:<8}{sim_prob:<24.4%}{analit_prob:<24.4%}")
