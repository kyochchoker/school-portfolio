#Ask the user for a word. 
# Print the number of uppercase letters in the word.

count = 0
uppercased = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

words  = input("Please input a word: ")

for i in words:  
    if i in uppercased:
        count += 1

print(f"Then umber of uppercased letters: {count}")

# Ask the user to enter a number 5 times. 
# Identify how many numbers are positive, negative, and zero.  
positive_count = 0
negative_count = 0
zero_count = 0

for i in range (5):
        num = int(input("Enter a Number: "))
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:  
            zero_count =+ 1


print (f"Positive Number  Counts are: {positive_count}")
print(f"Negative Number Counts are: {negative_count}")
print(f"Zero Number Counts are: {zero_count}")