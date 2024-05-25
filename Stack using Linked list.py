class Node:
    def __init__(self):
        self.Data = None
        self.Next = None

StackList = [Node() for i in range(10)]
Head = -1
Tail = -1
Free = 0

def initialize():
    global Free, Head, Tail
    for i in range(10):
        StackList[i].Data = ""
        StackList[i].Next = i + 1
    StackList[9].Next = -1
    Head = -1
    Tail = -1
    Free = 0

def Push(Value):
    global Free, Head, Tail, StackList
    if Free == -1:
        print("Stack OverFlow!")
    elif Free == 0:
        Head = Free
        Tail = Free
        StackList[Free].Data = Value
        Free = StackList[Free].Next
        StackList[Tail].Next = -1
    else:
        StackList[Free].Data = Value
        StackList[Tail].Next = Free
        Tail = Free
        Free = StackList[Free].Next
        StackList[Tail].Next = -1

def Pop():
    global Free, Head, Tail, StackList
    if Head == -1:
        print("Stack UnderFLow, Stack is empty")
        return -1
    elif Tail == Head:
        Result = StackList[Tail].Data
        StackList[Tail].Data = ""
        Head = -1
        StackList[Tail].Next = Free
        Free = Tail
        Tail = -1
        return Result
    else:
        Result = StackList[Tail].Data
        StackList[Tail].Data = ""
        StackList[Tail - 1].Next = -1
        StackList[Tail].Next = Free
        Free = Tail
        Tail -= 1
        return Result

def Display():
    global Free, Head, Tail, StackList
    if Head == -1:
        print("Stack is Empty")
    else:
        for i in range(len(StackList)-1,-1,-1):
            if i == Tail:
                print(StackList[i].Data,StackList[i].Next,"\t <---- Top")
            else:
                print(StackList[i].Data,StackList[i].Next)
        print("Header : ",Head)
        print("Tail : ",Tail)
        print("Free : ",Free)

initialize()
choice = 0
Info = Node()
while choice != 4:
    print("STACK MENU")
    print("1 : Push value onto the Stack")
    print("2 : Pop the value from the Stack")
    print("3 : Display Stack")
    print("4 : Exit Program")
    choice = int(input("Enter your Choice : "))
    if choice == 1:
        Data = input("Enter Data : ")
        Push(Data)
    elif choice == 2:
        Data = Pop()
        print("DATA POPPED : ",Data)
    elif choice == 3:
        Display()
    elif choice == 4:
        print("Exitting...")
    else:
        print("Invalid Choice ")
