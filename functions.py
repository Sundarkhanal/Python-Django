# def hello_func():
#     pass    #for filling function later
# print(hello_func())



# def hello_func():
#     print('Hello function')    #for filling function later
#     #print hello function 5 times
# hello_func()
# hello_func()
# hello_func()
# hello_func()
# hello_func()  


# def hello_func():
#     return'Hello function'   #for filling function later
#     #print hello function 5 times
# hello_func()
# print(hello_func().upper())   #print the function result


# def hello_func(greeting, name = 'you'):
#     return '{}, {}'.format(greeting, name)    #The format method places the greeting value at the {} placeholder and the name value at the second {} placeholder in the string.
# print(hello_func('Hi', name= 'sundar'))


# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)

# student_info('Math' , 'Art', name = 'Jhon', age =22)




# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
# courses = ['Math', 'art']
# info = {'name': 'Jhon', 'age': 22}

# student_info(*courses, **info)





month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year % 4 == 0  and (year % 100 != 0 or year % 400 == 0)
def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]
print(days_in_month(2017,2))