number_range = range(1,101)

for number in number_range:
    if number % 3 == 0 and number % 5 == 0:
        print ('FizzBuzz')
        continue
    elif number % 3 == 0:
        print ('Fizz')
        continue
    elif number % 5 == 0:
        print ('Buzz')
        continue
    else:
        print(number)

