# Program that only accepts numeric input

while True:
    answer = input("Enter a board size (x * x): ")

    # Check if input contains only digits
    if answer.isdigit():
        number = int(answer)
        print("You entered:", number, "*", number)
        break
    else:
        print("Invalid, please enter a number! ")