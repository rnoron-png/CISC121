# CyclicRotation - rotate list A to the right K times

def solution(A, K):
    n = len(A)
    if n == 0:
        return []

    result = [0] * n
    for i in range(n):
        # each element moves K spots right, % n wraps it back to the start
        new_index = (i + K) % n
        result[new_index] = A[i]

    return result


print(solution([3, 8, 9, 7, 6], 3))
print(solution([0, 0, 0], 1))
print(solution([1, 2, 3, 4], 4))
print(solution([], 5))
