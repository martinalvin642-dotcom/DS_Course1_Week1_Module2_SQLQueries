def temp_check(x):
    
    def valid(y):
        return -100 <= y <= 100

    def classify(y):
        if not valid(y):
            return "Invalid"
        if y < 25:
            return "Cold"
        return "Hot"

    return classify(x)


print(temp_check(26)) 
students =[{
    "name":"Diana",
    "age":20,
    "stud_id":69596

},
{
    "name":"alvin",
    "age":22,
    "stud_id":12349
},
{
    "name":"lewis",
    "age":33,
    "stud_id":20239

}]
print(students[1])
for student in students:
  print(f"{student["name"]},{student["age"]}")



file = open("notes.txt", "r")
