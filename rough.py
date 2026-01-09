stu = {
    "name" : "Rankumar",
    "L_name" : "Sharma",
    "age" : 21,
    "city" : "Indore",
    "subject"  : {
            "maths" : 78,
            "science" : 89,
            "english" : 90,

    },
            "email" : "dummy@gmail.com",
}


stu.update({"email" : "dummy@gmail.com"})
stu.keys()
print(stu.get("subject"))
stu.update({"subject" : {"hindi": 55}})
print (stu.get("subject"))

