# FrogJmp - smallest number of jumps of size D to get from X to Y or past it

def solution(X, Y, D):
    distance = Y - X
    jumps = distance // D

    # if there's any distance left over, one more jump is needed
    if distance % D != 0:
        jumps = jumps + 1

    return jumps


print(solution(10, 85, 30))
print(solution(10, 10, 5))
print(solution(1, 5, 2))
print(solution(5, 105, 3))
