def reverse (n):
    rev = 0
    while(n!= 0):
        rev = rev * 10
        rev = rev + n %10
        n = n/10
        return rev
A, B = input().split()
A = int(A)
B = int(B)
A = reverse(A)
B = reverse (B)
C = A + B
C = int(C)
print(reverse(C))