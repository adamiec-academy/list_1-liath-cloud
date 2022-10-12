def factorial(n):
   silnia = 1

   if n != 0:

       for i in range(1, n + 1):

           silnia *= i

   digits = len(str(silnia))
   space_1 = 3 - len(str(n))
   space_2 = 3 - len(str(digits))


   print(" " * space_1 + str(n) + "! is " + " " * space_2 + str(digits) + " digits long")
    

def report():
    for j in range(101):
        factorial(j)   
