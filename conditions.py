# if, else, elseif


# temp = int(input('type todays temp= '))

# if temp > 25:

#     print('Its too hot today')

# else:
#     print("Its confortable weather")        

#  ----------------------------

# temp = int(input('type todays temp= '))

# if temp > 40:

#     print('Its too hot today')

# elif 30 <= temp <= 40:
#     print("its worm wearther, wear light cloth")

# else:
#     print("Its confortable weather") 

input_taker = int(input('Please input a number: '))

if input_taker % 3 == 0 & input_taker % 5== 0:
    print('FizzBuzz')

elif input_taker % 3 == 0:
    print('Fizz')

elif input_taker % 5 ==0:
    print('Buzz')

else:
    print('output not a FizzBuzz number')