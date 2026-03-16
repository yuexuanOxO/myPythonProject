greeting = input("Say hi in English or Spanish! ")
greet_en =("hi", "Hi", "hello", "Hello")
greet_sp =("hola", "Hola")
if greeting not in greet_en and greeting not in greet_sp:
    print("I don't understand your greeting.")
elif greeting in greet_en:
  num = int(input("Enter 1 or 2: "))
  print("You speak English!")
  if num == 1:
      print("one")
  elif num == 2:
      print("two")
elif greeting in greet_sp:
    num = int(input("Enter 1 or 2: "))
    print("You speak Spanish!")
    if num == 1:
        print("uno")
    elif num == 2:
        print("dos")
