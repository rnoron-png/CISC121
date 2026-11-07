# OddOccurrencesInArray - find the value in A that has no matching pair

def solution(A):
    sorted_A = sorted(A)

    # after sorting, pairs sit next to each other, so check two at a time
    i = 0
    while i < len(sorted_A) - 1:
        if sorted_A[i] != sorted_A[i + 1]:
            return sorted_A[i]
        i = i + 2

    return sorted_A[len(sorted_A) - 1]


print(solution([9, 3, 9, 3, 9, 7, 9]))
print(solution([42]))
print(solution([5, 5, 1]))
print(solution([2, 2, 2]))
