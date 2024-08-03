# name = 'sundar'
# if name == 'sundar':
#     print('conditional was true')

# elif name == 'saroj':
#     print('conditional was false')

# elif name == 'john':
#     print('name is john')

# elif name == 'jane':
#     print('name is jane')


# else:
#     print('name is something else')

user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad credentials')



user = 'Admin'
logged_in = False
if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad credentials')



user = 'Admin'
logged_in = False

if not logged_in:
    print('Please log in')

else:
    print('Welcome to the page')



a = [1,2,3]
b = [1,2,3]
print(id(a))
print(id(b))
print(a is b)  
print(id(a) == id(b))

#False
condition = False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


#None
condition = None
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

#Zero of any numeric type
condition = 0
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


condition = 10
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

#Any empty sequence. For example, '', (), [].
condition = ()
if condition:
    print("Evalutaed to True")
else:
    print('Evaluated to Flase')

condition = 'sundar'
if condition:
    print("Evalutaed to True")
else:
    print('Evaluated to Flase')



#Any empty mapping. For example, {}.
condition = {}
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')