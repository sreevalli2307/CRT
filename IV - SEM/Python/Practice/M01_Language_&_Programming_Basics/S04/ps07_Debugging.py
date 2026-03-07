''' bug --> errors
Debugging --> Finding and Fixing of Errors
#Types of Errors:
1) syntax Errors --> missing of colon, missing of indentation.
2)Runtime Errors --> Division by Zero.
3)Logical Errors --> Missing of Logics.
Debugging Techniques:
1)print()
2) try-expect
3) Using pdb 
purpose:
1) pause the execution code
2)inspect the variable's value
3)to run the code line by line
Pdb Commands:
1)n -->to execute the output in a nextine
2)p variable --> to get the value of a variable
3)l --> list nearby code
4)c -->Continue the execution
5)s --> to start a function
6)r --> return from the function
7)h -->help
8)q -->quit the execution

try:
    a = int(input("enter a num: "))
    print(10/a)
except ZeroDivisionError:
    print("can not divisible by zero.")
except ValueError:
    print("Invalid input")
    '''
import pdb
def add(a,b):
    pdb.set_trace()
    return a+b 
a = int(input("Enter first number: "))
b = int(input("Enter second number:"))
print(add(a,b))