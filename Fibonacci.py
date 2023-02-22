print("""
**************************

Fibonacci Serisi Oluşturma

**************************



""")
limit = int(input("Kaç adet fibonacci sayısı olsun?  : "))
a = int(input("Sayı1 :"))
b = int(input("Sayı2 :"))
print(a)
print(b)

for i in range(limit-2):
    c=a+b
    a=b
    b=c
    print(c)

