'''1) write a program for the factors of a given number
n = int(input("enter a number: "))
count = 0
for i in range(1,n+1):
    if n%i==0:
        count+=1
        print(i,end=" ")
print("number of factors: ",count)
2) reverse a given number?
n = int(input())
if n>0:
    print(int(str(n)[::-1]))
else:
    n = -1*n
    print(-1 * int(str(n)[::-1]))
    3) check whether a given number is prime or not?

    '''
