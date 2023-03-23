#The Coding Starts With A Hello :)
firstName = input("Please Enter Your First Name: ")
fatherName = input("Please Enter Your Father's Name: ")
print("Hello,",firstName,fatherName,sep=' ', end = "\n")

#Random Inputs Which Can Be Used As Login System
username  = input("Please Enter Your Username: ")
password = input("Please Enter Your Password: ")

#Script To Check If Two Numbers Are Equal, First Number Is Less Than Or Greater Than Second Number
firstNumber = input("Please Enter First Number: ")
secondNumber = input("Please Enter Second Number: ")

if firstNumber < secondNumber:
    print("a<b")
elif firstNumber > secondNumber:
    print("a>b")
else:
    print("a=b")

#Script To Order From Menu
print("1. Soup & Salad")
print("2.Pasta with meat sauce")
print("3. Chef's special")

choice = int(input("Please Make a choice"))

if choice >=1 and choice <=3:
    if choice == 1:
        print("One Soup & Salad coming right up!")
    elif choice == 2:
        print("One Pasta with meat sauce coming right up!")
    else:
        print("One Chef's special coming right up!")
else:
    print("Invalid Input!")


#Script To Print Number Of Apples Each Person Possess Using Variables
john = 3
mary = 5
adam = 6
totalApples = john + mary + adam

print("John's Apples:"+ str(john) ,"Mary's Apples: "+str(mary),"Adam's Apples: "+str(adam),sep=" , ")
print("Total Apples are:",totalApples)

if totalApples >=10:
    print('Total apples are greater than 10.')
elif totalApples == 10:
    print('Total apples are equal to 10.')
else:
    print('Total apples are smaller than 10.')

#For Loops In Python
for i in range(10):
    print(i,end = " ")

print("\n")

#Range Function With Two Arguments
for i in range(1,10):
    print(i,end = " ")
print("\n")
    
#Range Function With Three Arguments
for i in range(10,1,-2):
    print(i,end = " ")
print("\n")

#While Loops In Python
i = 10
while i>0:
    print(i,end=" ")
    i-=1


#Function Definition & Calling In Python
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

firstNum = int(input("Please Enter First Number: "))
secondNum = int(input("Please Enter Second Number: "))

print(add(firstNum,secondNum))
print(subtract(firstNum,secondNum))

#Script To Find The Maximum Number Using Input, Loop & Function
def maxNum(num, maxium):
    max = maxium
    
    if num > max:
            max = num
    return max

maximum = 0
for i in range (0,10):
    num =  int(input("Enter The Number-"+str(i+1)+": "))
    maximum = maxNum(num,maximum)
print("Largest Number Is:",maximum)

#Lists & Their Methods In Python
list_ = [1,2,3,'AI',5.4]
print(type(list_))

#Accessing Values In Lists
print(list_[3])
print(list_[1:4])

#Assigning New Value To A List Index
list_[3] = 'Lab'
print(list_)

#Different Insertion Methods In List
list_.append(90)
list_.insert(3,'AI')
print(list_)

#Different Deleteion Methods In List
list_.pop(5)
list_.remove('AI')
print(list_)

#List Comprehension In Python
newList= [i*2 for i in range(1,6)]

#Script To Differentiate Even & Odd List Using List Comprehension
numbers = [int(input("Enter Number: ")) for i in range(1,10)]
evenList = []
oddList = []

for i in numbers:
    if i%2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)
print(evenList)
print(oddList)

#Strings In Python
#Slicing A String In Python
str ="AI Lab"
print(str[0:2])

#Converting A String In LowerCase & UpperCase
upper = str.upper()
print(upper)
lower = str.lower()
print(lower)

#Split & Map Function In Python
inputs = list(map(int,input().split(" ")))

#Script To Find The Length Of A String Without Using Len Function
target = "Awais Tanveer Khan"
length = 0

for letter in target:
    length += 1
print(length)

#Join Method In Python
lst = ['AI',"Lab"]
str2 = " ".join(lst)
print(str2)

#Tuples
tup = (2,3,4)

#Sets
set_ = {2,3,4}

#Dictionaries
person = {"firstName" : "Awais", "lastName": "Tanveer Khan","section":"6-A"}
print(person["firstName"])

#Printing Keys Of Dictionary
print(person.keys())

#Updating Value Of Dictionary Using It's Key
person["section"] = "6-A"
print(person)

#Adding Value In Dictionary
person["systemID"] = "NUML-F20-26171"
print(person)

#Deleting A Key-Value Pair From Dictionary
del person["systemID"]
print(person)

