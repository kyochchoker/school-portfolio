#1
num = int(input("Enmter a Number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *=i
print(f"The factorial of {num} is {factorial}")


#2
word = input("Enter a word: ")
num = int(input("How many times do you want it to print: "))
for i in range(num):
    print(word)