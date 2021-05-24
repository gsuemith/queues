a = [1, 2, 3, 4, 5, 6, 7]
k = 3

def foo(a, k):
  remainders = {}
  counter = 0
  for n in a:
    remainder = n % k
    print(n, remainders)
    if remainder in remainders:
      counter += remainders[remainder]

    converse = (k - remainder) % k
    if converse not in remainders:
      remainders[converse] = 0
    remainders[converse] += 1
  return counter

def sumsDivisibleByK(a, k):
    counter = 0
    for i in range(len(a)):
        for j in a[i+1:]:
            if (a[i] + j) % k == 0:
                counter += 1
    return counter

def bar(a,k):
  remainders = {}
  counter = 0
  for n in a:
    remainder = n % k
    


print(foo(a,k))
print(sumsDivisibleByK(a, k))