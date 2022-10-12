def factorial(n):
   silnia = 1

   if n != 0:

       for i in range(1, n + 1):

           silnia *= i

   return silnia
    

def report():
    for j in range(101):
        silnia = factorial(j)
        digits = len(str(silnia))
        space_1 = 3 - len(str(j))
        space_2 = 3 - len(str(digits))
        print(" " * space_1 + str(j) + "! is " + " " * space_2 + str(digits) + " digits long")

