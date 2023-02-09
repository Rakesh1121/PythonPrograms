a = {
    "name" : "Rakesh Vishwakarma",
    "age" : 45,
    "marks" : [50, 56, 48],
    "Profession": "Software engineer"
}

print(a)
#Lenght function
print(len(a))

#update the value 
#another way to update
a.update({"age": 23})
print(a)
a["age"] = 22
print(a)

#Printing the keys and values
x = a.keys()
y = a.values()
print(x)
print(y)

x = a.get("age")
print(x)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  
#for add key and value  
thisdict["Degree"] = "Bachlor of Engineering"
print(thisdict)

#for delete key and value
thisdict.pop("model")
print(thisdict)