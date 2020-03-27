def bubble_sort(s,f):
  for i in range(len(f)):
    for j in range(0,len(f)-i-1):
      if f[j] > f[j+1]:
        f[j], f[j+1] = f[j+1],f[j]
        s[j],s[j+1] = s[j+1],s[j]
  return s,f


def greedy(s,f,n):
  a = [True for x in range(n)]
  j = 0
  for i in range(1,n):
    if s[i] >= f[j]:
      a[i] = True
      j = i
    else:
      a[i] = False
  return a


while True:
    try:
        n = int(input())
    start = []
    end = []
    num = 0
    for i in range(n):
        x = input().split()
        start.append(int(x[0]))
        end.append(int(x[1]))
    start, end = bubble_sort(start, end)
    A = greedy(start,end,n)
    for k in range(len(A)):
    if A[k]:
        num+=1
    print(num)
    except EOFError:
        break
