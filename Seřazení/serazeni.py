A=int(input("Vlož hodnotu A:"))
B=int(input("Vlož hodnotu B:"))
C=int(input("Vlož hodnotu C:"))
P=0

if A<B:
    P=A
    A=B
    B=P
if B<C:
    P=B
    B=C
    C=P
if A<B:
    P=A
    A=B
    B=P

print(A,B,C)