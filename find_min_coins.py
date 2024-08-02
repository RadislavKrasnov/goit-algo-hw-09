
import sys
import timeit

def find_coins_greedy(value):
    if value == 0:
        return {}
    
    denominations = [50, 25, 10, 5, 2, 1]
    denominations.sort()
    n = len(denominations)
    result = {}
    i = n - 1
    while i >= 0:
        while value >= denominations[i]:
            denomination = denominations[i]
            value -= denomination
            if denomination in result:
                result[denomination] += 1
            else:
                result[denomination] = 1
        i -= 1
    
    return result

print(find_coins_greedy(113))

def find_min_coins(value):
    dp = [-1] * (value + 1)
    coins_count = [-1] * (value + 1)
    denominations = [50, 25, 10, 5, 2, 1]
    denominations.sort()
    n = len(denominations)
    min_coins = min_coins_util(denominations, n, value, dp, coins_count)

    result = {}

    if min_coins == sys.maxsize:
        return result  # No solution possible

    while value > 0:
        coin = coins_count[value]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        value -= coin
    
    return result

def min_coins_util(denominations, n, value, dp, coins_count):
    if value == 0:
        return 0
    
    if dp[value] != -1:
        return dp[value]
    
    result = sys.maxsize # represent the largest positive integer that a Python int can hold on the platform

    for i in range(n):
        if denominations[i] <= value:
            sub_result = min_coins_util(denominations, n, value - denominations[i], dp, coins_count)

            if sub_result != sys.maxsize and sub_result + 1 < result:
                result = sub_result + 1
                coins_count[value] = denominations[i]
    
    dp[value] = result

    return result

print(find_min_coins(113))

def evaluate_time_execution(cost):
    algorithms = [
        find_min_coins,
        find_coins_greedy
    ]

    for algorithm in algorithms:
        start = timeit.default_timer()
        algorithm(cost)
        end = timeit.default_timer()
        execution_time = end - start
        print(f"{algorithm.__name__} time execution for cost {cost} is {execution_time}")

costs = [113, 521, 995]

for cost in costs:
    evaluate_time_execution(cost)
