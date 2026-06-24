# # DICTIONARY

# #Learning Dictonary CRUD using vanilla python 

# # Vanilla Python means plain, standard Python without any third-party libraries, frameworks, or custom modifications.

# #Create dictionary
# dic = {
#     "name" : "Ana",
#     "age" : 23
# }

# #Assigning new key value to dictionary
# dic["profession"] = "Designer"

# #Read the key or value in dictionary
# print(dic["name"]) 

# #Updating the key value that already existing
# dic["profession"] = "Coder"

# #Deleting the key value from dictionary
# del dic["age"]

# for i in dic: # To access the keys
#     print(i)

# for i in dic.values(): # To access the values
#     print(i)

# for key, value in dic.items(): # To access the values keys
#     print(key," = ", value)

# #Methods
# d = {1:10,2:20,3:30,4:40,5:50,6:60,7:70,8:80}
 
# # 1) clear() Removes all the elements from the dictionary
# d.clear()
# print(d)

# d = {1:10,2:20,3:30,4:40}

# # 2) fromkey() Returns a dictionary with the specified keys and value. dict.fromkeys(keys, value) 
# # keys → An iterable containing the keys.
# # value → Optional. The value assigned to all keys (default is None).
# # fromkeys() is a dictionary method that creates a new dictionary using a group of keys and assigns the same value to all of them.

# q = d.fromkeys([9,10],95)
# print(q)

# # 3) get() 	Returns the value of the specified key
# print(d.get(1))

# # 4) items() Returns a list containing a tuple for each key value pair
# print(d.items()) #[(1, 10), (2, 20), (3, 30), (4, 40)]
# #Here items() convert key,value into tuple and dict{} convert into list

# # 5)keys() Returns a list containing the dictionary's keys
# print(d.keys()) #dict_keys([1, 2, 3, 4])

# # 6)pop() Removes the element with the specified key
# # poped = d.pop(4)
# # print(poped)
# # print(d)

# # 7) popitem() Removes the last inserted key-value pair
# # poped = d.popitem() 
# # print(poped) #(3, 30)
# # print(d)

# # 8) setdefalt() Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# d.setdefault(4,400)
# print(d)

# # 9) update() Updates the dictionary with the specified key-value pairs
# d.update({1:1000}) #update existing keys with updated value
# d.update({5:50}) #update new key, value
# print(d)

# #Questions on Dictionary 
# # 1)Merge two dictionaries into one.
d1= {"a":1, "b":2, "c":3, "d":4} 
d2= {"e":5, "f":6, "g":7, "h":8} 

# d1.update(d2) #using methods

for i in d2:
    d1[i]=d2[i]
print(d1)

#2)Sum all values in a dictionary.
d={"a":10,"b":20,"c":30}
sum = 0
for i in d.values():
    sum += i
print(f"Sum of all values in a dictionary is {sum}")

# 3)Count the frequency of each element in a list using a dictionary.
l = ["a","c","b","a","c","b","a","c","e","i"]
d = {}
for i in l:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
print(d)

# 4)Combine two dicts, adding values for common keys.
d1= {"a":1, "b":2, "c":3, "d":4} 
d2= {"e":5, "f":6, "g":7, "h":8, "a":12} 
for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i]
    else:
        d1[i] = d2[i]
print(d1)

# 5)Check if a key exists in a dictionary.
d= {"a":1, "b":2, "c":3, "d":4} 
if "a" in d.keys():
    print("key exists")
else:
    print("key does not exists")