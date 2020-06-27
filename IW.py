"""Input="google.com"
requireddic={ }
for i in Input:
    #print(i)
    if i in requireddic:
        #print(i)
        requireddic[i] += 1
    else:
        requireddic[i] = 1
print(requireddic)
"""
"""
Input= input("Enter the string")
if len(Input)<2:
    print("Empty String")
else:
    print (str(Input[0:2])+str(Input[-2:]))
    """

"""Input="ashutohakv"
first =Input[0]
print(Input[0])
Input= Input.replace(first,"$")
y=first+Input[1:]
print(y)
"""
"""x=input("Enter a first string")
y= input("enter seconf string")
"""

"""a="ashutosh"
b="saroj"
fristswap= b[:2] + a[2:]
print(fristswap)
secondswap= a[:2] + b[2:]
print(secondswap)
print(fristswap + " " + secondswap)"""

"""a=input("Enter a string")
#b=a[-3:]
#print(b)
if len(a)>1:
    print(a + "ing")
elif (a[-3:] == "ing"):
    print(a + "ly")
"""

"""a="The lyrics is not that poor!"
#a="The lyrics is poor"
b=a.find("not")
c=a.find("poor")
print(b)
print(c+4)
if b<c:
    #f=a.replace(a[14:-1],"good")
    a = a.replace(a[b:(c + 8)], 'good'+ "!")
print(a)"""

"""a=[]
for i in range(0,5):
    b=input("enter a string to append")
    str(a.append(b))
    #print(x)
    i=i+1
print(a)
j=[]
for k in a:
    j.append((k,len(k)))
    j.sort()
print(j)
print(j[0])
"""

"""
def remove(string, n):
    first = string[:n]
    last = string[n + 1:]
    return first + last


word = input("Enter the word:")
n = int(input("Enter the index of the character to remove:"))
print("Modified word:")
print(remove(word, n))
"""


"""def change(a):
    return a[-1:] + a[1:-1] + a[:1]


print(change('ashutosh'))
"""

"""def modify(string):
  final = ""
  for i in range(len(string)):
    if i % 2 == 0:
      final = final + string[i]
  return final
string=input("Enter string:")
print("Modified string is:")
print(modify(string))
"""
"""def ULcase(string):
    up=string.upper()
    lo=string.lower()
    return up,lo
print(ULcase("worksheet"))
"""
"""
a=[]
for i in range(0,5):
    b=input("enter a string to append")
    str(a.append(b))
    #print(x)
    i=i+1
print(a)
j=[]
t=[]
for k in a:
    j.append(k)
    t.append(len(k))
    t.sort(key=int)
    j.sort(key=len)
    x=t[-1:]
print(t)
print(j)"""

"""
list=[]
a=input("enter the length of list")
for i in range(int(a)):
    b = input("enter a string to append")
    list.append(b)
print(list)

x=1
for j in list:
    x=int(j)*x
print(x)"""

"""list=[]
a=input("enter the length of list")
for i in range(int(a)):
    b = input("enter a string to append")
    list.append(b)
print(list)

x=0
for j in list:
   x=int(j)+x
print(x)
"""
"""
insert_sting_middle=[[[]]]
a=input('enter a string')
c=insert_sting_middle[0][0]
print(c)

print(c.append(a))
print(c)
print(insert_sting_middle)
"""
"""
SampleList= ['abc', 'xyz', 'aba', '1221']
c=0
for i in SampleList:
    x=[i]
    if x[0][0]==x[0][-1]:
        c=c+1
print(c)
"""
"""
a="[[]]"
b="{{}}"
hey="A"
print(a[:2] + hey + a[2:]) # TRY TRY TRY

def insertstring(string,word):
    return string[:2]+ word+ string[2:]
print(insertstring("[[]]","Ashutosh"))
print(insertstring("{{}}","Kumar"))
print(insertstring("<<>>","Verma"))"""

"""list = [23, 450, 1, 4, 89]
print(range(len(list)))
x=0
for i in range(len(list)):
    print(list[i])
    if list[i]>x:
        x=list[i]
print("greatest number is :", x)"""

"""list = [23, 450, 189, 4, 89]
print(range(len(list)))
x=list[0]
for i in range(len(list)):
    print(list[i])
    if list[i]<x:
        x=list[i]
print("Smallest number is :", x)
"""

#QUES21
"""
list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

List1 =[]
List2 =[]

for k in list:
    List1.append(k[1])

List1.sort()

for i in List1:
    for j in list:
        if i == int(j[1]):
            List2.append(j)

print(List2)

"""

#QUES22
"""list=[24,25,26,25,26,21,24,22]
x=[]
for i in list:
    if i not in x:
        x.append(i)
print(x)
"""
#Ques23
"""
list=[23,24,25,26," ", 27]

for i in list:
    if i == " ":
        list.remove(i)
print(list)
if len(list)==0:
    print ("list is empty")
else:
    print ("list is not empty")
"""
#ques24
"""
list =[{},{},{}]
print(all( len(d) == 0 for d in list))
for i in list:
    if len(i)==0:
        print("list is empty")
    else:
        print("list is not empty")

"""
#QUES 25

"""list=[1,2,3,4]
x=[]
for i in list:
    #print(i)
    b="emp{}".format(i)
    #print(b)
    x.append(b)
print(x)"""

#QUES26

"""sample1= [1, 3, 5, 7, 9, 10]
sample2=[2, 4, 6, 8]
sample1[-1:]=sample2
print(sample1)"""
#QUES27
"""
sample1={0: 10, 1: 20}
sample1[2]=30
print(sample1)
"""
#QUES29
"""
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)
"""
#ques30 and 31 and 35
"""
sample = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(sample.items())
for i in sample:
    print(i,sample[i])
def test(x):
  if x in sample:
      print("yes!! it is present")
  else:
      print("oops!")
test(4)
test(8)
"""
#QUES32and 33
"""
output={}
#print(output.items())
for i in range(1,15):
    output[i] = i*i
print(output)
"""
#QUES34
"""
dic1={"brand":"ford", "model":"Mustang"}
dic2={"color":"red", "mileage":40}

dic4={}
for d in (dic1, dic2): dic4.update(d)
print(dic4)
"""

#QUE36 and 37
"""
sample = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(sample.items())
x=0
y=0
z=1
for i in sample:
    print(i,sample[i])
    y=y+i
    x=x+sample[i]
    z=z*sample[i]
print(y,x)
print(z)
"""
#qQUES 38
"""
word = {
    "Hello": 56,
    "lets" : 23 ,
    "use" : 43,
    "them" : 43
    }
if "use" in word:
    del word["use"]
if "them" in word:
    result = word.pop("them", None)

print("Updated Dictionary :", word)
"""
#ques39
"""
x=(1,2,3,4,5)
(nirmal,saroj,ghimire,verma,Ashutosh)=x
print(nirmal)
print(Ashutosh)
print(ghimire)
"""
#QUES40,41,42
"""
x=(1,2,3,4,5)
y=("1","2","3","4","5")
z=[1,2,3,4,5]
b=x+ (9,)
list1=list(x)
tuple1=tuple(z)
str =  ''.join(y)
print(list1)
print(b)
print(str)
print(z)
"""

#QUES43,44,45,46
"""
sample=("ashutosh", 1, "verma", 2,"saroj",3)
x=list(sample)
delete=x.remove("verma")
print("DELETE OF TUPLE")
print(tuple(x))
print("````````````")
print("SLICING")
slice=x[1:4]
print(tuple(slice))
print("````````````")
print("LENGTH")
length1=len(sample)
print(length1)
print("````````````")
print("INDEX VALUES")
index1=sample.index("verma")
index2=sample.index("saroj")
index3=sample.index(1)
print(index1)
print(index2)
print(index3)
"""
#QUES FUNCTIONS 1
"""
def maxi(range1):
    sample=[]
    x=1
    for i in range(int(range1)):
        b=input("enter the list")
        sample.append(int(b))
        if sample[i]>x:
            x=sample[i]
    return x
print("the maximum number is",maxi(5))
"""
#QUES FUNCTIONS 2
"""
def sum(range1):
    sample=[]
    x=0
    for i in range(int(range1)):
        b=input("enter the list")
        sample.append(int(b))
        x=sample[i]+x
    return x
print("the sum of all  number is",sum(5))

"""
#QUES FUNCTIONS 3
"""
def sum(range1):
    sample=[]
    x=1
    for i in range(int(range1)):
        b=input("enter the list")
        sample.append(int(b))
        x=sample[i]*x
    return x
print("the multiplication of all  number is",sum(5))
"""
#QUES FUNCTIONS 4
"""
def rev(str):
    strlen=len(str)
    newstr=str[strlen::-1]
    if newstr==str:
        print("palindrome")
    else:
        print("nope!!")
    return newstr
print("REVERSE STRING",rev(input("enter a string")))
"""

#QUES FUNCTIONS 5
"""
def facto(n):
    if n == 0:
        return 1
    else:
        return n * facto(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(facto(n))
"""

#QUES FUNCTIONS 6
"""
def find(sample):
    upper=0
    lower=0
    for c in sample:
            if c.isupper():
                upper=upper+1
            elif c.islower():
                lower=lower+1
    print(upper)
    print(lower)
find("AshuToshKumarVerma")
"""
#QUES FUNCTIONS 8
"""
def unique_list(l):
  new = []
  for a in l:
    if a not in new:
      new.append(a)
  return new
print(unique_list([1,2,3,3,3,3,4,5]))
"""
#QUES FUNCTIONS 10
"""
def even(SampleList):
    x=[]
    for i in SampleList:

        if (i % 2) == 0:
            x.append(i)
    return x

print("Even numbers from given list",even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
"""
#QUES FUNCTIONS 11
"""
try1 = lambda x : x + 15
print("Addition in lambda function is:",(try1(3)))
print("`````````````````````")
try2 = lambda x, y : x * y
print("Multiplication is:",(try2(2, 9)))
"""
#QUES FUNCTIONS 12
"""
def unk(ran):
     b=input("enter a random number to be multiplied")
     x=int(ran) * int(b)
     return x
print("MULTIPLICATION WITH UNKNOWN NUMBER IS", unk(2))
"""
#QUES FUNCTIONS 13
"""
sample=[("name",90),("firstname",12),("surname",14),("middlename",60),("ashutosh",10)]
sample.sort(key= (lambda x : x[1]))
print(sample)
"""
#QUES FUNCTIONS 14
"""
sample=[{"age":90},{"age":12},{"age":14},{"age":60},{"age":10}]
#sample.sort(key= (lambda x : x[1]))
#print(sample[0].values())

sample.sort(key= lambda x: x["age"])
print(sample)
"""
#QUES FUNCTIONS 15 and 16
"""
def even(SampleList):
    b=list(filter(lambda x: (x % 2 == 0), SampleList))
    return b
def mul(Sample):
    c=list(map(lambda x: x**2, Sample))
    return c


print("Even numbers from given list",even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print("sqaure of  from given list",mul([1, 2, 3, 4, 5, 6, 7, 8, 9]))
"""
#QUES FUNCTIONS 17
"""
x="ashutosh"
print(x[0])
if ( x[0]=="b"):
    print("true")
else:
    print("false")
print("```````````````")
string = "ashutosh"
print(string.startswith("a"))
print("`````````````````")
is_num = lambda q: q.isdigit()
print(is_num('9842042640'))
print(is_num('98511aaaa1'))
"""
#QUES FUNCTIONS 19
"""
def fibonacci(count):
    list = [0, 1]
    print(sum(list[-1:]))
    any(map(lambda a : list.append(sum(list[-2:])),
            range(2, count)))
    return list[:count]
print(fibonacci(10))
"""
#QUES FUNCTIONS 20
"""
sample1=[1,2,3,4,5,6,7,8,9]
sample2=[3,4,5,6,11,55,66,99]
x=[]
for i in sample1:
    if i  in sample2:
        x.append(i)
print(x)
print("!!!!!!!!!!!!!!!!!!!!!!!")
c=[]
c=list(filter(lambda a: a in sample2, sample1))
print(c)
"""
#   "THANK YOU FOR THIS ASSIGNMENT MODULE IT HAS BEEN VERY HELPFUL!!!!!"















































