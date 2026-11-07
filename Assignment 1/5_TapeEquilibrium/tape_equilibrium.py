# TapeEquilibrium - find the split of A with the smallest |left sum - right sum|

def solution(A):
    total = sum(A)

    # first split: A[0] on the left, everything else on the right
    left_sum = A[0]
    right_sum = total - A[0]
    smallest = abs(left_sum - right_sum)

    # move the split right one spot at a time instead of re-adding everything
    for i in range(2, len(A)):
        left_sum = left_sum + A[i - 1]
        right_sum = right_sum - A[i - 1]
        difference = abs(left_sum - right_sum)
        if difference < smallest:
            smallest = difference

    return smallest


print(solution([3, 1, 2, 4, 3]))
print(solution([1, 2]))
print(solution([-1000, 1000]))
print(solution([5, -5, 5, -5]))
