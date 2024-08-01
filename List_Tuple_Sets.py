courses = ['math', 'science', 'nepali']
print(courses)
print(len(courses))
print(courses[-1])
print(courses[0:3])
print(courses[0])


#modifying lists using insert mathod
courses = ['math', 'science', 'nepali']
courses_2 = ['art', 'education']
courses.insert(0,courses_2)

# courses.append('english')
# courses.insert(0,'Web')
# courses.insert(1,'Account')
# courses.insert(2,'Web')
print(courses)

#by using extend method()
courses = ['math', 'science', 'nepali']
courses_2 = ['art', 'education']
courses.extend(courses_2)
print(courses)

#removing items form lists
courses = ['math', 'science', 'nepali']
courses.remove('math')              #removes specific items

print(courses)

#removing items by using pop method
courses = ['math', 'science', 'nepali']
courses.pop()          #removes last items
popped = courses.pop()   #gives removed value
print(popped)

print(courses)

#shorting the list
courses = ['math', 'science', 'nepali']
num = [1,2,3,4,5]
num.sort(reverse= True)
print(num)
courses.reverse()
courses.sort(reverse= True)
sorted_courses = sorted(courses)
print(sorted_courses)
print(courses)
print(courses)

#printing max and min numbers
num = [1,2,3,4,5]
print(max(num))
print(min(num))
print (sum(num))