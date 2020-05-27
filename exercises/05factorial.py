# Write a method to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example method call
#
# factorial(5)
#
# > 120
#

def factorial(number):
        if number == 1:
            var = 1 
        elif number == 0:
            var = 0
        else:       
            for i in range (2,number):
                var = i*number
    
        return var


fact = factorial(5)

print("factorial",fact)       

