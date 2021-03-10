def sum(n):
   if n <= 1:
    return n
   else:
    return n + sum(n-1)


num = 44

if num < 0:
   print("Please enter a positive integer")
else:
   print("The sum is",sum(num))
    
    
Output: 
The sum is 990 
