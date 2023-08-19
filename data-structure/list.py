# note that in python, array and list is different
# list is actually and ADT that creator of Python create to let us use it easily

mylist = [5,6,2,7,2,4,7,3,8]
print('new list')
print(mylist)
print('============================')



# Add to List
mylist.append("apple")
print('append')
print(mylist)
print('============================')

mylist.insert(2, "kiwi")
print('insert')
print(mylist)
print('============================')

list1 = ['banana', 'cherry']
mylist.extend(list1)
print('extend')
print(mylist)
print('============================')



# Remove from List
mylist.remove('banana')
print('remove')
print(mylist)
print('============================')

mylist.pop()
print('pop()')
print(mylist)
print('============================')

mylist.pop(3)
print('pop(n)')
print(mylist)
print('============================')

mylist.clear()
print('clear')
print(mylist)
print('============================')



# Loop in List
mylist = [5,6,2,7,2,4,7,3,8]

for x in mylist:
    print(x)

for i in range(len(mylist)):
    print(str(i) + ' ' + str(mylist[i]))



# Sort List
mylist.sort()
print('sort')
print(mylist)
print('============================')

mylist.sort(reverse=True)
print('reverse sort')
print(mylist)
print('============================')

mylist = [5,6,2,7,2,4,7,3,8]
mylist.reverse()
print('reverse order')
print(mylist)
print('============================')



# Split String into List
text = 'the weather is so beautiful today'
# Split on 'space'
newlist = text.split(' ')
print('split string')
print(text)
print(newlist)
print('============================')



# Join List into String with space
newtext = ' # '.join(newlist)
print('join list')
print(newtext)
print('============================')