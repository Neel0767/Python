dict = {'name': 'Neel', 'project' : 'library managment', 'age' : 19 , 'camera' : 16 }

print("keys is : ", dict.keys())
print("values is: ", dict.values())
print("items is: ", dict.items())
print()
print(f"popping a key-value pair : {dict.pop('project')}")
print(f"new dict is: {dict}")
print("length is  : ", len(dict))
print("sorted     : ", sorted(dict))