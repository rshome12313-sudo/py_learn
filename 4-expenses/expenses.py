expenses = [10.2, 32.2, 32.7, 45.4, 23.32, 98.2, 32.1]

expenses_sum = sum(expenses)
expenses_min = min(expenses)
expenses_max = max(expenses)
expenses_mean = expenses_sum / len(expenses)

print(
    (
        expenses_sum,
        expenses_mean,
        expenses_min,
        expenses_max,
    )
)
