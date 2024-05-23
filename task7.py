import random
import matplotlib.pyplot as plt
import seaborn as sns

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

def plot_probabilities(probabilities, title):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    sns.barplot(x=sums, y=probs, palette='viridis', edgecolor='black', label='Simulation')
    
    for i, prob in enumerate(probs):
        plt.text(i, prob + 0.001, f"{prob:.2%}", ha='center', va='bottom')

    plt.xlabel('Sum of Dice', fontsize=12)
    plt.ylabel('Probability', fontsize=12)
    plt.title(title, fontsize=15)
    plt.xticks(sums)
    plt.ylim(0, 0.2)
    
    analytical_probs = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
        7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }
    
    plt.plot(sums, [analytical_probs[sum_] for sum_ in sums], 'r--', label='Analytical')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

# Кількість симуляцій
num_rolls = 1000000

# Виконуємо симуляцію
sum_counts, probabilities = simulate_rolls(num_rolls)

# Виводимо результати
print("Sum\tSimulated Probability\tAnalytical Probability")
analytical_probs = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}
for sum_, prob in probabilities.items():
    print(f"{sum_}\t{prob:.4%}\t\t\t{analytical_probs[sum_]:.4%}")

# Побудова графіка
plot_probabilities(probabilities, "Probability of Sums of Two Dice Rolls (Monte Carlo Simulation)")
