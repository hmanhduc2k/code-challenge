def nSum_iterative(input):
    s = 0
    for i in range(1, input + 1):
        s = s + i
    return s
# Runtime: O(n) iterate

def nSum_recursive(input):
    if input == 0:
        return 0
    return input + nSum_recursive(input - 1)
# Runtime: O(n) recursive

def nSum_constant(input):
    s = input * (input + 1) // 2
    return s
# Runtime: O(1)

print(nSum_iterative(10), nSum_recursive(10), nSum_constant(10))