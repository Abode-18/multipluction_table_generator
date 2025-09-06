# the project is a program that write the result of the numbers between the 2 numbers that the user enters multiplayed by the numbers 1-10
#2/8/2025 by: Abdulrahman alowidi and the help of mohamad

import sys
#the process(function)
def multiplaying_table():
    
    #checking input number 1:a
    a=input("enter starting num ")
    if a =="":
        print("enter a vailed number")
        sys.exit()
    elif a.isdigit() :
        a=int(a)
    else:
        print("enter a vailed number")
        sys.exit()

    
    #checking input number 2: b
    b=input("enter ending num ")
    if b =="":
        print("enter a vailed number")
        sys.exit()
    elif b.isdigit() :
        b=int(b)
    else:
        print("enter a vailed number")
        sys.exit()
    
    # checking that the ending number is more than the starting number
    if b<a:
        print(" the ending number must be more than the starting number ")
        sys.exit()
    #the multiplaying process
    for x in range(a,b+1):
        for y in range(1,11):
            r = x*y
            print(f"{x}x{y}={r}")

multiplaying_table()