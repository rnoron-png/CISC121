# PermMissingElem - A has the numbers 1 to N+1 with one missing, find it

def solution(A):
    n = len(A)

    # sum of 1 to N+1 using Gauss's formula
    expected_total = (n + 1) * (n + 2) // 2

    actual_total = 0
    for value in A:
        actual_total = actual_total + value

    return expected_total - actual_total


print(solution([2, 3, 1, 5]))
print(solution([]))
print(solution([1]))
print(solution([2]))
