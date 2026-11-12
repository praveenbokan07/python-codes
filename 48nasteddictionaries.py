student = {
    "name" : "praveen gurjar",
    "score" : {
           "phy" : 99,
           "chem" : 98,
           "math" : 100,
    },   
}
print(student)
print(student["score"])
print(student["score"]["math"])
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
print(student.get("age"))
student.update({"age" : 19,"name" : "golu"})
print(student)