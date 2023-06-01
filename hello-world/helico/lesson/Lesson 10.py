

def fak(x):
    if x == 0:
        return 1
    return fak(x - 1) * x

#def fac(i):
 #   if i == 0:
  #      return 1
   # return fac(i - 1) * i

n = int(input())
q = (fak(n))

res = []

for i in range(q):
    res.append(i)
print(res)

    #f = q - 1
    #print(f)


d = (fac(i))

print(d)