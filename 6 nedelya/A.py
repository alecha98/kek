N=int(input())
k=1
A=list(map(int, input().split()))
for i in range (N):
    a=A[i]
    for j in range (k,N):
        b=A[j]
        if a==b:
            print(a)
    k+=1