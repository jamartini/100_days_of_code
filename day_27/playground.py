def add(*nums):
    result = 0
    for n in nums:
        result += n
    return result


print(add(1, 1, 2, 3, 5, 8, 13, 21))
