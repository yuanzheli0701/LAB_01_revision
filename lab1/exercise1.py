def reverse_integer(n):
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = (reversed_n * 10) + digit
        n //= 10
    return reversed_n

print(reverse_integer(315))
print(reverse_integer(400))
print(reverse_integer(101))