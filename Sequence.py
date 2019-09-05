#Design an algorithm that generates the first n numbers in the following 
# sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

n = int(input("Enter the length of the sequence: "))

counter =3 
num1 =1 
num2=2
num3=3
print(num1)
print(num2)
print(num3)
while counter <= n-1:
    summa=num1+num2+num3
    print(summa)
    counter +=1
    num1 = num2
    num2 = num3
    num3 = summa