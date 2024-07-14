d={}#Empty Dictionary
marks = {
    "Harry":100,
    "Rohan": 56,
    "Shubham": 23,
    0: "Harry"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry": 98, "Renuka": 100})
# print(marks)

print(marks.get("Harry2")) #Prints none
print(marks["Harry2"]) #Returns and error