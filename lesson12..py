# print('Hello')


# def numeric(oldfilename:str, newfilename:str) -> None:
#     try:
#         with open(oldfilename, 'r') as file:
#             res = file.readlines()
#         with open(newfilename, 'a') as file:
#             for i in range(0, len(res)):
#                 file.write(f'{i + 1}) - {res[i]}')
#     except FileNotFoundError:
#         return 'Error'
# oldfilename = input('Enter old file name: ')
# newfilename = input('Enter new file name: ')
# numeric(oldfilename, newfilename)

# def max_item_lenght(filename:str) -> str:
#     mylist = []
#     try:
#         with open(filename, 'r') as file:
#             res = file.readlines()
#         for i in res:
#             i = i.replace('\n', '')
#             mylist.append(i)
#         mylist.sort(key=len)
#         for i in mylist:
#             if len(i) == len(mylist[-1]):
#                 print(i)
#     except FileNotFoundError:
#         print('No File')

# max_item_lenght('users.txt')


# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# [[
#     1, 2, 3, 4, 
#     8, 7, 6, 5,
#     9, 10, 11, 12
# ]]

