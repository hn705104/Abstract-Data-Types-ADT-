#Global Variables:
LP = [None for i in range(10)]
Data = [None for i in range(10)]
RP = [None for i in range(10)]
Null = -1
Free = 0

def InitializeBT():
    for i in range(10):
        LP[i] = Null
        Data[i] =''
        RP[i] = Null
    global Free
    Free = 0

def AddDataBt(Value):
    global Free
    if Free == 10:
        print("Binary Tree is full")
    elif Free == 0:
        Data[Free] = Value
        Free = Free + 1
    else:
        CurrentNode = 0
        Data[Free] = Value
        while CurrentNode != -1:
            PrevNode = CurrentNode
            if Value < Data[CurrentNode]:
                CurrentNode = LP[CurrentNode]
                Direction = 'L'
            elif Value > Data[CurrentNode]:
                CurrentNode = RP[CurrentNode]
                Direction = 'R'

        if Direction == 'L':
            LP[PrevNode] = Free
        elif Direction == 'R':
            RP[PrevNode] = Free
        Free += 1

def SearchBt(Value):
    Root = 0
    while CurrentNode != Null:
        if Data[CurrentNode] == Value:
            return CurrentNode
        elif Value < Data[CurrentNode]:
            CurrentNode = LP[CurrentNode]
        else:
            CurrentNode = RP[CurrentNode]

    if CurrentNode == Null:
        print("Value does not exist")
        return -1

def DisplayBT():
    print("LP\t","DATA\t","RP")
    for i in range(10):
        print(LP[i],"\t",Data[i],"\t",RP[i])

def InorderTraversaal(root):
    global Null
    if root != Null:
        InorderTraversaal(LP[int(root)])
        print(Data[int(root)])
        InorderTraversaal(RP[int(root)])

def PreorderTraversal(root):
    global Null
    if root != Null:
        print(Data[int(root)])
        PreorderTraversal(LP[int(root)])
        PreorderTraversal(RP[int(root)])

def PostorderTraversal(root):
    global Null
    if root != Null:
        PostorderTraversal(LP[int(root)])
        PostorderTraversal(RP[int(root)])
        print(Data[int(root)])



InitializeBT()
choice = 0
while choice != 7:
    print("1 : Add Data in BT")
    print("2 : Display Data in BT")
    print("3 : Search Data in BT")
    print("4 : Pre Order Traversal")
    print("5 : In Order Traversal")
    print("6 : Post Order Traversal")
    print("7 : Exit Program")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        info = int(input("Enter Data to input in BT"))
        AddDataBt(info)
    elif choice == 2:
        DisplayBT()
    elif choice == 3:
        search = input("Enter Data to search")
        result = SearchBt(search)
        print(result)
    elif choice == 4:
        PreorderTraversal(0)
    elif choice == 5:
        InorderTraversaal(0)
    elif choice == 6:
        PostorderTraversal(0)
    elif choice == 7:
        print("Exitting...")
    else:
        print("Invalid choice")



