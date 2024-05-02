# Question 1

number = input("Enter a number: ")

if number > "0":
    print("The number is positive.")
elif number == "0":
    print("The number is zero.")
elif number < "0": print("The number is negative.")


# Question 2 Task 1

num = int(input("Please insert a number here: "))
num2 = int(input("Please insert a number here: ")) 
num3 = int(input("Please insert a number here: "))
highest_number = max(num, num2, num3)
print(f"The largest number is {highest_number}")
    

# Question 2 Task 2

num = int(input("Please insert a number here: "))
num2 = int(input("Please insert a number here: ")) 
num3 = int(input("Please insert a number here: "))
highest_number = max(num, num2, num3)
lowest_number = min(num, num2, num3)
print(f"The largest number is {highest_number}. The smallest number is {lowest_number}")

