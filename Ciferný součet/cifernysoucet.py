n=int(input("Zadej přirozené č.:"))
soucet=0

while n>0:
    cifra=n%10
    soucet += cifra
    n //= 10

print("Ciferný součet:", soucet)