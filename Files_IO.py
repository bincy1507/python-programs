# my_file = open('./test.txt.txt')
# print(my_file)
# print(my_file.readlines())
# print(my_file.readline())
# my_file.close()

# Read,write,append

# with open('./test.txt.txt',mode='r') as my_file:
#     print(my_file.readline())
#     print(my_file.readlines())

# with open('./test.txt.txt',mode='r+') as my_file:
#     text = my_file.write('I am 24 now')
#     print(my_file.readline())
#     print(my_file.readline())
#     print(my_file.readline())
#     print(my_file.readline())
#     print(my_file.readlines())

# with open('./test.txt.txt',mode='a') as my_file:
#     text = my_file.write('I am looking out for job oppurtunities')
#     print(text)

# with open('./test.txt.txt',mode='w') as my_file:
#     text = my_file.write('Love what u do, do what u love')
#     print(text)

#FILE I/O ERRORS
# try:
#     with open('./sad.txt',mode='r+') as my_file:
#         print(my_file.read())
# except FileNotFoundError as err:
#     print('File not found')
#     raise err
# except IOError as e:
#     print('Input-Output error')
#     raise e

