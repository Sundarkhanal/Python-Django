nums = [0,1,2,3,4,5,6,7,8,9]

# # I want 'n' for each 'n' in nums
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# my_list = [n for n in nums]
# print(my_list)  

# I want 'n*n' for each 'n'  in nums
# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

# my_list = [n*n for n in nums]
# print(my_list)   

# Using map+ lambda
#   # Example list of numbers
# my_list = map(lambda n: n*n, nums)
# print(list(my_list))  # Convert the map object to a list and print it


# I want 'n' for each 'n' in nums if 'n' is even
# my_list = []
# for n in nums:
#     if n % 2 == 0:
#         my_list.append(n)
# print(my_list)

#    OR
# my_list = [n for n in nums if n % 2 == 0]
# print(my_list)


# # Using a filter + lambda
# my_list = filter(lambda n: n%2 == 0,nums)
# print(list(my_list))


# I want a (letter, num) pair for each letter in 'abcd' and each number in '04123'
# my_List = []
# for letter in 'abcd':
#     for num in range(4):
#         my_List.append((letter, num))
# print(my_List)


# #    oR
# my_List = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_List)


# Dictionary Comprehensions
# names = ['Ram','Shyam', 'Hari', 'Gopal', 'Sita',]
# heros = ['Batman','Superman', 'Spiderman', 'Wolverine', "Deadpool"]
# zipped_list = zip(names, heros)
# print(list(zipped_list))


# I want a dict{'name': 'hero'} for each name, hero in zip(names, heros)
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print(my_dict)


# my_dict = {names: heros for  names, heros in zip(names, heros) }
# print(my_dict)

# # if name not equal to ram
# my_dict = {names: heros for  names, heros in zip(names, heros) if names != 'Ram' }
# print(my_dict)



# Set comprehensions

# nums = [1,2,2,3,1,4,5,6,2,1,4,7,9,6,3,5,4]
# my_set  = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)   #gives us unique value

# my_set = {n for n in nums}
# print(my_set)   #gives us unique value

# Generator Expressions

# I want to yield 'n*n' for each 'n' in nums
def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)
for i in my_gen:
    print (i)


my_gen = (n*n for n in nums)
for i in my_gen:
    print (i)