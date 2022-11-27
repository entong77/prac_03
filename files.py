#  1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
out_file = open("name.txt", 'w')
name1 = input("Please enter your name: ")
out_file.write(name1)
out_file.close()

# 2. Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).
open_file = open("name.txt", "r")
name2 = open_file.read()
print("Your name is ", name2)
open_file.close()

# 3. reads only the first two numbers and adds them together then prints the result, which should be... 59.
open_file = open("numbers.txt", "r")
number1 = int(open_file.readline())
number2 = int(open_file.readline())
print(number1 + number2)
open_file.close()

# 4. write a code that prints the total for all lines in numbers.txt or a file with any number of numbers.
open_file = open("numbers.txt", "r")
total = 0
for line in open_file:
    total += int(line)
print(total)
open_file.close()

