def factorial(x): # функция для получения факториала из числа
    if x == 0:
        return 1
    return factorial(x - 1) * x

res = []

n = int(input())
f1 = factorial(n) 

while f1 >= 1:   
    f1 -= 1
    f2 = factorial(f1 + 1)
    res.append(f2)

print(res)