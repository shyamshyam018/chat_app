while True:
    user_input = input("Enter a number: ")
    
    try:
        number = int(user_input)
    except ValueError:
        print("Try other number")
        continue

    if number == 0:
        print("Game over!")
        break
    elif number > 100:
        print("Exiting the program.")
        exit()
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print("Try other number")
