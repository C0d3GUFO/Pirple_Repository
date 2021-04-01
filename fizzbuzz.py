
for num in range (1, 101):
    if num > 1:
    #First we check for the prime numbers conditions.
       for i in range(2, num):
           if (num % i) == 0:
    #Here check for Fizz, Buzz and FizzBuzz conditions.
               if num%3 == 0 and num%5 == 0:
                   print("FizzBuzz")
               elif num%3 == 0:
                   print("Fizz")
               elif num%5 == 0:
                   print("Buzz")

               else:
                   print(num)
               break
       else:
           print("prime")
#Print number 1 which is not a prime number.
    else:
       print(num)
