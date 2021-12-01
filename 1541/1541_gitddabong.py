# import sys
# input = sys.stdin.readline

# input_list = list(input().rstrip())
# num = ['0', '1', '2', '3', '4', '5', '6', '7', '8' ,'9']

# temp = ''
# calc_li = []
# for str in input_list:
#     if str in num:
#         temp += str
#     else:
#         calc_li.append(int(temp))
#         temp = ''
#         calc_li.append(str)
# calc_li.append(temp)

# while len(calc_li) > 1:
#     for i in range(len(calc_li)):
#         if calc_li[i] == "+":
#             sum = calc_li[i-1] + calc_li[i+1]
#             calc_li[i-1] = sum
#             calc_li.pop(i)
#             calc_li.pop(i+1)
            
#         if calc_li[i] == "-":
#             sub = calc_li[i-1] - calc_li[i+1]
#             calc_li[i-1] = sub
#             calc_li.pop(i)
#             calc_li.pop(i+1)

# print(calc_li[0])

import sys
input = sys.stdin.readline

input_list = list(input().split('-'))
nums = []
for element in input_list:
    sum = 0
    sentence = element.split('+')
    for num in sentence:
        sum += int(num)
    nums.append(sum)

result = nums[0]
for i in range(1, len(nums)):
    result -= nums[i]

print(result)