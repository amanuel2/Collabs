# Python Factorial
# Author-Amanuel Bogale
# Date 5/27/2016



def factorial(x,total):
    while(x!=0):
        total = (total) + ((x) * (x-1));
        x-=1;
        if(x==1):
            print(total)


total = 0;
print(factorial(5,total));
