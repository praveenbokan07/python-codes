info = {
    "name" : "praveen",
    "cgpa" : 9.6,
    "marks" : [98,99,100],  
}
print(info)
print(info["name"])
print(info["cgpa"])
print(info["marks"])
info["cgpa"] = 9.8 #change the value
info["city"] = "jaipur" #add new key
print(info)