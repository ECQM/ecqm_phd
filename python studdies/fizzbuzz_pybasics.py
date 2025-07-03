#practicing python basics , functions and maths
import math
#print("hello world")
#def AddTwoNumbers(n1, n2):
#    Budget=n1+n2
#    return int(Budget)
#print(AddTwoNumbers.__doc__)
#def exchange_money(Budget,exchange_rate):
#    exchange_budget=Budget*exchange_rate
#    return int(exchange_budget)
#def get_number_of_bills(exchange_budget,smallest_denomination):
#    calculate_change=exchange_budget%smallest_denomination
#    number_of_bills=(exchange_budget-calculate_change)/smallest_denomination
#    return int(calculate_change,number_of_bills)
#def return_change(calculate_change,exchange_rate):
#    change=calculate_change*1/exchange_rate
#    return int(change)
lower_bound = 0
upper_bound = 1000

# FIZZBUZZ
def fizzbuzz(lower_bound,upper_bound):
    x = lower_bound 
    numbers = list()
    while x<upper_bound:
        output = str('')
        if x % 3 == 0:
            output = output + str('Fizz')
        if x % 5 == 0:
            output = output + str('Buzz')
        if x % 7 == 0:
            output = output + str('Biff')
        if x % 11 == 0:
            output = output + str('Zip')
            x = x+1
        list.append(output)
    with open("fizzbuzz.txt", "w") as output:
        output.write(numbers)