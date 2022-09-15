def missing_number(nums: list[int]) -> int:
    n = len(nums)
    total = sum(nums)
    return (n * (n + 1) / 2) - total

print(missing_number([0, 1, 2, 3]))

print(missing_number([3, 0, 1]))