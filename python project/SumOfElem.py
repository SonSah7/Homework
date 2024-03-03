def sumOfelems(numbers, exclude_negative=False):
    total = 0
    for num in numbers:
        if not exclude_negative or num >= 0:
            total += num
    return total

input_numbers = input("Enter a list of numbers separated by spaces: ")
numbers_list = [int(num) for num in input_numbers.split()]
    
exclude_choice = input("Do you want to exclude negative numbers? (yes/no): ").strip().lower()
exclude_negative = exclude_choice == 'yes'

total_sum = sumOfelems(numbers_list, exclude_negative)
print("Sum of the elements:", total_sum)

