# allows us to work with a list of values and peform operations on them.

courses = ['history','maths','physics','comp science']
nums = [1,2,3,4,5,6]

print(courses)

print(nums)

# you want to get how many values you have in the list len
print(len(courses))
print(len(nums))

#to access members in a list indexing begin from 0
print(courses[0])

#list modification
#append add a new member to the list
courses.append('biology')
print(courses)
#add a member to a specific location
courses.insert(2,'chemistry')
print(courses)

#remove delete a value at a particular index
courses.remove('physics')
print(courses)

#pop remove the last value on list
lastvalue=courses.pop()
print(lastvalue)

#sorting list

courses.sort()
nums.sort()
nums.sort(reverse=True)
courses.sort(reverse=True)
print(nums)
print(courses)

print(min(nums))
print(max(nums))
print(sum(nums))

#Loops in lists
for item in courses:
    print(item)
    
#enumerate gives both index and value
for index, course in enumerate(courses):
    print(index, course)

