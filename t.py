x = [2, 4]
x = x * 3
# print(x[3])


nums = [4, 7, 3, 1]
# for x in nums:
    # print(x*2)

x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
sum = 0
for a in x:
    sum += a
print(sum)

nums = list(range(5))
print(nums[4])

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4])

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])

nums = [1, 2, 3, 4, 5, 6]
res = nums[::-1]
print(res[2])

x = [6, 4, 2, 9]
x = x[::-1]
print(x[0]+x[2])

list = [8, 4, 2, 6]
list.remove(2)
print(len(list)+list.count(6))

nums = [2, 4, 8, 9, 5]

nums.insert(1, 3)
nums.remove(9)
nums.insert(0, nums.count(8))
print(nums[3])

txt = "hello"
print(max(txt))


def sum(x):
    res = 0
    for i in range(x):
        res += i
    return res


print(sum(4))
