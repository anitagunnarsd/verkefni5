#Maximum number
#Design an algorithm that finds the maximum positive integer input by a user.  
#The user repeatedly inputs numbers until a negative value is entered.

num_int = int(input("Input a number: "))

counter=0

while num_int >-1:
    if num_int> counter:
        counter = num_int
    num_int = int(input("Input a number: "))
print("The maximum is", counter)