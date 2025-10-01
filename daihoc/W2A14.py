def swap(num1, num2):
    return num2, num1

a, b = map(int, input().split())

a, b = swap(a, b)

print(a, b)