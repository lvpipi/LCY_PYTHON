a=[x for x in range(1000) if x%2==0]
print(a)

start_list = [5, 3, 1, 2, 4]
square_list = []
# Your code here!
for number in start_list:
	start_list.append(number)
print (start_list)

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print (list(filter(lambda x: x != 'Python', languages)))
print ([x for x in languages if x != 'Python'])

