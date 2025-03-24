#prompt the user to enter 5 numbers. Store them in a list.
#Display the list as entered, small to large, and large to small
#Calculate and display the mean and median
#This is a guided practice. You can follow the video or your instructor will go
#over this in class


# Prompt the user to enter 5 numbers
numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Display the list as entered
print(f"The list as entered: {numbers}")

# Display the list sorted from small to large
sorted_numbers = sorted(numbers)
print(f"The list from small to large: {sorted_numbers}")

# Display the list sorted from large to small
sorted_numbers_desc = sorted(numbers, reverse=True)
print(f"The list from large to small: {sorted_numbers_desc}")

# Calculate and display the mean
mean = sum(numbers) / len(numbers)
print(f"The mean of the numbers is: {mean}")

# Calculate and display the median
if len(sorted_numbers) % 2 == 0:
    median = (sorted_numbers[len(sorted_numbers)//2 - 1] + sorted_numbers[len(sorted_numbers)//2]) / 2
else:
    median = sorted_numbers[len(sorted_numbers)//2]
print(f"The median of the numbers is: {median}")
