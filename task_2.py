def chess_board(n, k):
   first_pattern = (" " * k + "#" * k) * n
   second_pattern = ("#" * k + " " * k) * n

   flag = 0

   for i in range(n * 2):

       if flag == 0:
           for j in range(k):
               print(first_pattern)
           flag = 1
       else:
           for j in range(k):
               print(second_pattern)
           flag = 0
