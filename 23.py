__author__ = 'student'
A=input().split()
for i in range(len(A)):
    A[i] = int(A[i])
B = max(A)
C = A.index(B)
print(B, C)