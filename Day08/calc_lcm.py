#!/usr/bin/env python3

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return abs(x * y) // gcd(x, y)

def calculate_lcm(numbers):
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required to calculate LCM")

    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])
    
    return result

# Example usage:
# num_list = [12, 18, 24, 36]
num_list = [13301,18961,16697,17263,12169,14999]


result = calculate_lcm(num_list)
print(f"The least common multiple of {num_list} is {result}")