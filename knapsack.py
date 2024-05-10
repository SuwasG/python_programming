'''

Suppose you are organizing a picnic with your friends, and you have a budget constraint. You want to buy different items such as sandwiches, drinks, fruits, and snacks for the picnic. Each item has its own price, and you want to maximize the variety of items while staying within your budget. How can you use Python to determine the optimal combination of items to purchase to make the picnic enjoyable without exceeding your budget?

'''


def knapsack(items, budget):
    n=len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)] #This line is using a list comprehension to create a 2D list dp (dynamic programming table) to store the maximum value that can be achieved for different budgets and different numbers of items. dp with n + 1 rows and budget + 1 columns, initialized with zeros

    for i in range(1, n+1):
        for j in range(1,budget+1):
            item_price, item_value= items[i-1]
            if item_price>j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_price] + item_value)

        max_value = dp[n][budget]
        selected_items = []

    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            item_price, item_value = items[i - 1]
            selected_items.append((item_price, item_value))
            j -= item_price

    return max_value, selected_items

# Example usage:
items = [(10, 60),  # (price, value)
         (20, 100),
         (30, 120),
         (15, 70)]

budget = 50

max_value, selected_items = knapsack(items, budget)

print("Optimal combination of items within budget:")
for item_price, item_value in selected_items:
    print(f"Price: {item_price}, Value: {item_value}")

print("Total value of selected items:", max_value)