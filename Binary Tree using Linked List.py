#Implementation of binary tree using linked list:
class LinkedList:
    def __init__(self):
        self.LP = 0
        self.Data = 0
        self.RP = 0

BT = [LinkedList() for i in range(10)]
Free = 0

#Procedure to initialize the Binary tree
def Initialize():
    global BT, Free, Header, Tail
    Free = 0
    for i in range(10):
        BT[i].LP = i + 1
        BT[i].RP = -1
    BT[9].LP = -1

#Function to add data in the BT
Root = -1
def AddData(Value):
    global BT, Free, Root
    Dir = ''
    if Free == 10:
        print("OverFlow, BinaryTree is full")
    elif Free == 0:
        BT[Free].Data = Value
        BT[Free].LP = -1
        Root = Free
        Free += 1
    else:
        BT[Free].Data = Value
        BT[Free].LP = -1
        CurrNode = Root
        PrevNode = -1

        while CurrNode != -1:
            PrevNode = CurrNode
            if Value < BT[CurrNode].Data:
                Dir = 'L'
                CurrNode = BT[CurrNode].LP
            elif Value > BT[CurrNode].Data:
                Dir = 'R'
                CurrNode = BT[CurrNode].RP

        if Dir == 'L':
            BT[PrevNode].LP = Free
        elif Dir == 'R':
            BT[PrevNode].RP = Free

        Free += 1
        print("Data Succesfully Added")

#Procedure to dislay Binary Tree
def DisplayBT():
    print("Free : ", Free)
    print("LP     Data     RP")
    for i in range(10):
        print(BT[i].LP," ",BT[i].Data," ",BT[i].RP)

choice = -1
Initialize()
while choice != 3:
    print("Add Data in Binary tree : 1")
    print("Display Binary Tree : 2")
    print("Exit Program : 3")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        Data = input("Enter the value to be added")
        AddData(Data)
    elif choice == 2:
        DisplayBT()
    elif choice == 3:
        print("Exitting Program")
    else:
        print("Invalid Choice")

