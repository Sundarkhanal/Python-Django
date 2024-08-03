student = {'name': 'sundar', 'age': '25', 'courses': ['Math', 'Science']}
print(student)
print(student['name'])
print(student['age'])
print(student['courses'])

print(student.get('name'))
print(student.get('phone')) #get method gives none if the items is not in the dictionary
print(student.get('phone','Not found'))   #providing default value 


#updating value in dictionary
student = {'name': 'sundar', 'age': '25', 'courses': ['Math', 'Science']}
student['name'] = 'jhon'
print(student)


#using update method
student = {'name': 'sundar', 'age': '25', 'courses': ['Math', 'Science']}
student.update({'name':'saroj', 'age':'12',})
print(student)

#deleting any item in dictionary
student = {'name':'sundar','age':'16','courses':'math'}
del student['age']
print(student)


#removind items form pop method
student = {'name':'sundar','age':'16','courses':'math'}
age = student.pop('age')
print(age)
print(student)
print(len(student))
print(student.values())
print(student.keys())
print(student.items()) #returns list of tuples


#printing key using for loop
student = {'name':'jhon', 'age': '12'}
for key in student:
    print(key)

#printing key and values
student = {'name':'jhon', 'age': '12'}
for key,values in student.items():
    print(key,values)



