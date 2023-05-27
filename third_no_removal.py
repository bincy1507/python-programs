# def remove_nums(int_list):
#     #list starts with 0 index
#     idx = 0
#     len_list = (len(int_list))
#     while len_list>0:
#         idx = (2+idx)%len_list
#         print(int_list.pop(idx))
#         len_list -= 1
# nums = [10,20,30,40,50,60,70,80,90]
# remove_nums(nums)

nums = [10,20,30,40,50,60,70,80,90]
idx = 0
n = len(nums)
for i in range(n,0,-1):
    idx = (2+idx)%i
    print(nums.pop(idx))
