number = int(input("Enter nummber from 1 to 100: "))
if number > 0 or number <100:
    if number % 3 == 0:
        print("Fizz")
        if number % 5 == 0:
            print("Buzz")
            if number % 3 == 0 and number % 5 == 0:
                print("Fizz" +  "Buzz")
print("Error")