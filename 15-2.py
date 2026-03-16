do = input("輸入: ")
if do == "LOOK":   
    print("You are stuck in a sand ditch.")
    print("Crawl out LEFT or RIGHT.")
    do = input(":: ")
    if do == "LEFT":   
        print("You make it out and see a ship!")
        print("You survived!")
    elif do == "RIGHT":   
        print("No can do. That side is very slippery.")
    print("You fall very far into some weird cavern.")
    print("You do not survive :(")
else:
    print("You can only do actions shown in capital letters.")
    print("Try again!")
