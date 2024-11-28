def reverse(num):
    result = 0
    while num > 0:
        result = (result << 1) | (num & 1)
        num >>= 1
    return result

n = int(input("Enter number: "))
reversed_num = reverse(n)
print(f"Reversed number: {reversed_num}")
