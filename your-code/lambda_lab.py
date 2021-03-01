l = [2,4,5,6,7,1,3,2,3,9]

def cosa (l):
	ls = []
	for num in l:
		ls.append(num*2)
	return ls

print(cosa(l))

"""
No funciona
#ls = []
#f = (lambda l:ls.append(x*2) for x in l)
#print (f)
"""


#f = list(map(lambda x: x * 2 , l))

f = lambda x: x*2

#no entiendo porque hay que ponerle la variable X a lambda - es porque tiene map supongo

b = []


def modify_list(l, f):
    for x in l:
        b.append(f(x))
    return b

print(modify_list(l, f))


#duda de git
"""
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   08-comprehensions.ipynb
	modified:   09b-functions-II-&-lambdas.ipynb
"""
"""
lst = [2, 3, 4]
b = []
def modify_list(lst, fudduLambda):
    for x in lst:
        b.append(fudduLambda(x))


modify_list(lst, fudduLambda)


#Call modify_list(##,##)
#print b
"""

#Now we will define a lambda expression that will transform the elements of the list.
#lambda expression that converts Celsius to Kelvin. 

#example lambda

double = lambda x: x * 2
print(double(5))

l = [1, 2, 3, 4, 5, 6, 7]

t = lambda l: l + 2

print(t)



#mod = lambda x,y: print(1) if x%y == 0 else print (0)

division_lambda = lambda num, denom: (num / denom) if denom != 0 else None
division_lambda(5, 0)


mod = lambda x,y: 1 if x%y == 0 else 0

print (mod(2,2))




#Define a simple lambda expression for eg that updates a number by 2

#### Now create a function that returns mod. 
#The function only takes one argument - 
#the first number in the `mod` lambda function. 


list1 = ['Green', 'cheese', 'English', 'tomato']
list2 = ['eggs', 'cheese', 'cucumber', 'tomato']
zipped = zip(list1,list2)
print(list(zipped))


list1 = [1,2,3,4]
list2 = [2,3,4,5]
## Zip the lists together 
zipped = zip(list1, list2)
## Print the zipped list 
print(list(zipped))

z = list(zipped)

for n in z:
	if n[0] == n[1]:
		print (n[0])
		print ("yes")
	else:
		print (n[0])
		print (n[1])
		print ("no")



list1 = ['Engineering', 'Computer Science', 'Political Science', 'Mathematics']
list2 = ['Lab', 'Homework', 'Essay', 'Module']


zipped = zip(list1, list2)

print(zipped)


sorted_zip = sorted(zipped, key = lambda x: x[0])


"""

d = {'Honda': 1997, 'Toyota': 1995, 'Audi': 2001, 'BMW': 2005}

sorted_valuess = sorted(d.items(), key= lambda item: item[1])
print (sorted_valuess)

dict1 = {1: 1, 2: 9, 3: 4}
sorted_tuples = sorted(dict1.items(), key=lambda x: x[1])

print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]

sorted_dict = {k: v for k, v in sorted_tuples}

print(sorted_dict)  # {1: 1, 3: 4, 2: 9}


"""



