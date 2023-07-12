# print("programming is fun ")
# x="ali"
# print(x)
# x=2
# print(x)
# x= input("what is your name \n")
# if x=="ahmed":
#     print("Hi")
#     print("welcome")
# else:
#     print("error ")
#     print("error not ahmed ")

# x=int(input("how old are you \n"))
# if x >15:
#     print("go get an ID")
# else:
#     print("still young")
# x = input("what is your name \n")
# if x == "ahmed":
#     f = input("enter your father name\n")
#     if f == "emad":
#         age = int(input("please ya ahmed enter your age \n"))
#         if age > 15:
#             print("great your big")
#         else:
#             print("oh still young")
#     else:
#         print("please make sure from your father name ")
# else:
#     print("incorrect user name ")
# number=int(input("please enter a number \n"))
# if number>1:
#     for i in range (2,number):
#         if number %i==0:
#             print("this number is not prim ")
#             break
#         else:
#             print("this number is prim ")
#
#
# else:
#     print("this is a not prime number ")

# names=["ahmed","omar","ali","abdullah"]
# for name in names:
#     if name=="ali":
#         print("rejected")
#     else:
#         print(name)

# numbers=[1,2,3,4,5,6,7,8,9,10]
# game_is_on=True
# while game_is_on:
#     if len(numbers)>=15:
#         game_is_on=False
#     search=int(input("enter a num"))
#     # if search in numbers:
#     #     print("found")
#     # else:
#     #     print("not found")
#     found=False
#     for n in numbers:
#         if n==search:
#             found=True
#             break
#     if found:
#         print("found")
#     else:
#         print("not")
#         numbers.append(search)
#         print(numbers)
# diction={
#     "key":"value",
#
# }
# print(diction["key"])
english_marks={
    "ahmed":20,
    "ali":40,
    "mohamed":50
}
# for key in english_marks:
#     print(key)
#     if english_marks[key]<25:
#         print("f")
#         if english_marks[key] >=25 and english_marks[key]<=35:
#             print("a")
#     else :
#         print("a+")
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}
#Nesting a List in a Dictionary

# travel_log = {
#   "France": ["Paris", "Lille", "Dijon"],
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }
# cities=[]
# ans=input("hi could you tell me about the city you want to search for \n")
# for key in travel_log:
#     if key.lower()==ans.lower():
#         cities=travel_log[key]
# if cities:
#     for i in cities:
#         print(i)
# else:
#     print("i will add this city put please give me three cities you saw them there \n")
#     list=[]
#     for i in range (3):
#         answer=input(f"enter the {i+1} city ")
#         list.append(answer)
#     travel_log[ans]=list
#     print(travel_log)
# travel_log = {
#   "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }
#
# for key in travel_log:
#     if key=="France":
#         target=travel_log[key]
#         cities=target["cities_visited"]
#         total=target["total_visits"]
#         for i in cities:
#             print(f" you have visted {i} {total} times  ")
# s="hello world"
# d={}
# for c in s:
#     if c in d:
#         d[c]+=1
#     else:
#         d[c]=1
# print(d)
#

def add(x,y):
    return x+y


def minus(x,y):
    if x>y:
        return x-y
    else:
        return y-x
def check (x):
    x=add(x,3)
    if x%2==0:
        return True
    else:return False

def rechecl(y):
    return check(y)
def dived():
    x= int(input("enter the first num \n"))
    y=int(input("enter the second number \n"))
    ans =input("what you wanna make add or check even or minus \n")
    if ans=="add":
        print(add(x,y))
    if ans =="check":
        c=int(input("enter the number you want to check \n"))
        print(check(c))
dived()
"incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "The programming language 'Python' is based off a modified version of 'JavaScript'",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "AMD created the first consumer 64-bit processor.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "'HTML' stands for Hypertext Markup Language.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "hard",
        "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    }
]

