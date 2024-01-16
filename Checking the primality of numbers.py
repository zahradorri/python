Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def is_prime(num):
...     if num <= 1:
...         return False
...     for i in range(2, int(num**0.5) + 1):
...         if num % i == 0:
...             return False
...     return True
... 
... num = int(input("Enter a number: "))
... if is_prime(num):
...     print(num, "is a prime number.")
... else:
