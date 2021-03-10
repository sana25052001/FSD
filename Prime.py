first = 400
last = 500

print("Prime numbers between", first, "and", last, "are:")

for num in range(first, last + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

Output :  Prime numbers between 400 and 500 are:                                                                                                                   
401                                                                                                                                                      
409                                                                                                                                                      
419                                                                                                                                                      
421                                                                                                                                                      
431                                                                                                                                                      
433                                                                                                                                                      
439                                                                                                                                                      
443                                                                                                                                                      
449                                                                                                                                                      
457                                                                                                                                                      
461                                                                                                                                                      
463                                                                                                                                                      
467                                                                                                                                                      
479                                                                                                                                                      
487                                                                                                                                                      
491                                                                                                                                                      
499                         
