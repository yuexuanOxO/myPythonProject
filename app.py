import sys ,random

print(sys.version)
print("Hello ",end="")
print("World!")

print("------------------------")
print(5+6)

print(type(True))


x,y,z = "OxO","Like","Game"
i = j = k = "哭阿"
print(x,y,z)
print(i,j,k)

print("------------------------")
fruits = ["apple","banana","cherry"]
x,y,z = fruits

print(x,y,z)
print("------------------------")

x = "awesome"

def myfunc():
    global x #global將區域變數變成全域變數
    x = "fantastic"
    print("Python is",x)

myfunc()

print("Python is",x)
print("------------------------")

x = ("apple", "banana", "cherryOxO")

#display x:
print(x[2])

#display the data type of x:
print(type(x)) 
print("------------------------")

x = {"name": "John", "age": 36}
print(x["age"])
print("------------------------")
unique_ids = set([1,1,2,3])
print(unique_ids)

print("------------------------")
x = frozenset({"apple", "banana"})
print(type(x))

print("------------------------")
x = b"Hello"
print(type(x))

print("------------------------")

x = 1
y = 2.5
z = 1j

a = float(x)
b = int(y)
c = complex(x)
print(a,b,c)

print(type(a))
print(type(b))
print(type(c))

print("------------------------")


print(random.randrange(1,10))

print("------------------------")

a = "Hello, World!"
print(a[8])

print("------------------------")
for x in range(6):
  print(x)
else:
  print("Finally finished!")


print("------------------------")
for x in [0, 1, 2]:
  print(x)

for i in range(5):
   pass


print("------------------------")
# 字串長度
a = "Hello, World!"
print(len(a))


print("------------------------")
#檢查字串
txt = "The best things in life are free!"
print("是否包含free:","free" in txt)

if "free" in txt:
  print("Yes, 'free' is present.")

print("------------------------")

#Check if NOT(是否不包含)
txt = "The best things in life are free!"
print("是否不包含expensive:","expensive" not in txt)

if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

if "free" in txt:
  print("Yes, 'free' is present.")