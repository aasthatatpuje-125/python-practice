try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter a number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

finally:
    print("Program finished.")