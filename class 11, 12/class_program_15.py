n = int(input("enter value: "))
rev = 0
while n:
    r=n%10
    n = n//10
    rev=(rev*10)+r
print(rev)
