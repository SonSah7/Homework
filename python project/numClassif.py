def classify_numbers(nums):
    evens = []
    odds = []

    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    return evens, odds

def main():
    user_input = input("Enter a list of numbers separated by spaces: ")
    nums = [int(x) for x in user_input.split()]

    even, odd = classify_numbers(nums)

    print("Even numbers:", even)
    print("Odd numbers:", odd)

if __name__ == "__main__":
    main()


