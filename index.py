# DICTIONARY

#Learning Dictonary CRUD using vanilla python 

# Vanilla Python means plain, standard Python without any third-party libraries, frameworks, or custom modifications.

#Create dictionary
dic = {
    "name" : "Ana",
    "age" : 23
}

#Assigning new key value to dictionary
dic["profession"] = "Designer"

#Read the key or value in dictionary
print(dic["name"]) 

#Updating the key value that already existing
dic["profession"] = "Coder"

#Deleting the key value from dictionary
del dic["age"]

for i in dic: # To access the keys
    print(i)

for i in dic.values(): # To access the values
    print(i)

for key, value in dic.items(): # To access the values keys
    print(key," = ", value)

#Methods
d = {1:10,2:20,3:30,4:40,5:50,6:60,7:70,8:80}
 
# 1) clear() Removes all the elements from the dictionary
d.clear()
print(d)

d = {1:10,2:20,3:30,4:40}

# 2) fromkey() Returns a dictionary with the specified keys and value. dict.fromkeys(keys, value) 
# keys → An iterable containing the keys.
# value → Optional. The value assigned to all keys (default is None).
# fromkeys() is a dictionary method that creates a new dictionary using a group of keys and assigns the same value to all of them.

q = d.fromkeys([9,10],95)
print(q)

# 3) get() 	Returns the value of the specified key
print(d.get(1))

# 4) items() Returns a list containing a tuple for each key value pair
print(d.items()) #[(1, 10), (2, 20), (3, 30), (4, 40)]
#Here items() convert key,value into tuple and dict{} convert into list

# 5)keys() Returns a list containing the dictionary's keys
print(d.keys()) #dict_keys([1, 2, 3, 4])

# 6)pop() Removes the element with the specified key
# poped = d.pop(4)
# print(poped)
# print(d)

# 7) popitem() Removes the last inserted key-value pair
# poped = d.popitem() 
# print(poped) #(3, 30)
# print(d)

# 8) setdefalt() Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
d.setdefault(4,400)
print(d)

# 9) update() Updates the dictionary with the specified key-value pairs
d.update({1:1000}) #update existing keys with updated value
d.update({5:50}) #update new key, value
print(d)




# You're studying tutorials but not building projects.
# You're learning too many things and mastering none.

# Python
# SQL
# APIs
# Pandas basics
# Automation scripts

