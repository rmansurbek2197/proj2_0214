# 6
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)

# 7
n = int(input())
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# 8
n = int(input())
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print("YES")
else:
    print("NO")

# 9
n = int(input())
s = input()
rev = s[::-1]
if s == rev:
    print("YES")
else:
    print("NO")

# 10
n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
main_diag = 0
sec_diag = 0
for i in range(n):
    main_diag += matrix[i][i]
    sec_diag += matrix[i][n - i - 1]
print(main_diag, sec_diag)
