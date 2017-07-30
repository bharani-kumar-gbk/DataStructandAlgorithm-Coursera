# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)


result = 0

f = max(a)
a.remove(f)
fa = max(a)

result = fa * f

print(result)
