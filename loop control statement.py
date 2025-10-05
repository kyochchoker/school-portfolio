#Ask the user to enter 10 numbers one by one. 
# Stop asking if the user enters 0, and print "Loop stopped."
for i in range (10):
    number = int (input(f"Enter number {i + 1}: "))

    if number  == 0:
        print("Loop Stopped early.")
        break

#Ask the user for 5 numbers. 
# Print only the positive numbers and skip the negative ones.

for i in range (5):
    number = int (input(f"Enter number {i + 1}: "))

    if number > 0:
        print(number)
    else:
        pass

#Write a loop that goes from 1 to 10. If the number is even, 
# just use pass (do nothing). Print the number otherwise.

for number in range (1 , 11):

    if number % 2 == 0:
        pass
    else:
        print(f"The odd numbers are {number}")


