'''
1) arithmetic progression values upto 10
t = int(input("enter a number:"))
d = int(input())
for i in range(10):
    print(t+(i*d),end = " ")
2) wrie a code for fibbonacci series using list
a =0
b =1
n = int(input())
for i in range(n):
    print(a,end= " ")
    a,b = b,a+b
    
li = [0,1]
for i in range(2,n):
    li.append(li[i-2]+li[i-1])
print(li)
3) write a code for power of a number
'''
n = int(input())
for i in range(1,11):
    print(n**i,end = " ")

