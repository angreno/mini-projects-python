import random
print("welcome to guessing the goat ")
name = input("please type your name to continue: ")

a = int(input("type you number 1: "))
b= int (input("type you number 2: "))


c= int(input("type you guessing number: "))
d=random.randint(a,b)
if(c == d):
    print("haha great",name, " you won the game ")
else:
    print("better luck next time","the number was",d)