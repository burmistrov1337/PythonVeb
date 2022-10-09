# Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя

nums = [1, 5, 2, 3, 4, 6, 1, 7]

def get_up1(nums):
    ups = [nums[0]]
    for i in nums:
        list02 = []
        list02.append(min(nums))
        for j in (i, len(nums)):
            if i > max(ups):
                ups.append(i)
            
    return ups

# # ups = []
# # def get_up2(nums):
# #     nums = list(filter(lambda x: ups not in x, nums.split()))
# #     print (nums)
# #     return " ".join(nums) 

# print(get_up1(nums))


list01 = [1, 5, 2, 3, 4, 6, 1, 7]
list01 = list(map(int, list01))

#k = 0
for i in range(len(list01)):
    list02 = []
    list02.append(min(list01))
    for j in range(i, len(list01)):
        if list02[-1] < list01[j]:
            #k += 1
            list02.append(list01[j])
    print(list02)



# def get_minmax(nums):
#     ups = []
#     ups.append(min(nums))
#     ups.append(max(nums))
#     return ups


# def get_1234(nums):
#     ups = []
#     ups.append(nums[0])
#     j = 0
#     for i in range(len(nums)):
#         if nums[i] == ups[j]+1 and nums[i] not in ups:
#             ups.append(nums[i])
#             j += 1
#     return ups


# def get_up(nums):
#     ups = []
#     for i in range(len(nums)):
#         if nums[i] == max(nums[:i+1:]) and nums[i] not in ups:
#             ups.append(nums[i])
#     return ups


# print(get_minmax(nums))
# print(get_1234(nums))
# print(get_up(nums))

