def envelope(n):
   max_length = 2 * n + 1
   middle_no = max_length - 4
   quarter_length = 0

   top_bottom = "*" * max_length

   print(top_bottom)

   for i in range(1, max_length - 1):

       if i < ((max_length - 2)// 2) + 1:

           print( "*" +  " " * quarter_length + "*" + " " * middle_no + "*" + " " * quarter_length + "*")

           quarter_length += 1
           middle_no -= 2


       elif i == (max_length - 2)// 2 + 1:

           print( "*" + " " * ((max_length - 3)//2) + "*" + " " * ((max_length - 3)//2) + "*")

       else:

           quarter_length -= 1
           middle_no += 2

           print( "*" +  " " * quarter_length + "*" + " " * middle_no + "*" + " " * quarter_length + "*")


   print(top_bottom)
