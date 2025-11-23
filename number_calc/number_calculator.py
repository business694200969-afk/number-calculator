import math
nums = []
while True:
    num = int(input("Enter number between 1 to 100. (press 0 to stop): " ))
    num_count = len(nums) + 1
    print("You wrote this amount of numbers", num_count)
    nums.append(num)
    if num == 0:
        nums.remove(0)
        break
    elif num > 100 or num < 1:
        print("Number must be in between 1 to 100!")
        num = int(input("Enter number between 1 to 100. (press 0 to stop): " ))


symbol = input("Enter symbol: (+, -, /, *, **) ")

if symbol == "+":
    sum1 = sum(nums)
    print("Sum of numbers you wrote is:", sum1)

elif symbol == "-":
    if num_count == 3:
        print(nums[0] - nums[1])
    if num_count == 4:
        print(nums[0] - nums[1] - nums[3])
    if num_count == 5:
        print(nums[0] - nums[1] - nums[2] - nums[3])
    if num_count == 6:
        print(nums[0] - nums[1] - nums[2] - nums[3])

elif symbol == "*":
    result = math.prod(nums)
    print(result)

elif symbol == "/":
    if num_count == 3:
        print(nums[0] / nums[1])
    elif num_count == 4:
        print(nums[0] / nums[1] / nums[2])
    elif num_count == 5:
        print(nums[0] / nums[1] / nums[2] / nums[3])
    elif num_count == 6:
        print(nums[0] / nums[1] / nums[2] / nums[3] / nums[4])
