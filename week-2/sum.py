print("Enter the size :")
size = int(input())
nums = []
for i in range(size):
    print("Enter element ", i+1, ":")
    nums.append(int(input()))


def add(nums):
    sum= 0 
    for i in range(len(nums)):
        sum += nums[i]
    return sum
   
print(f"The Result is {add(nums)}")
