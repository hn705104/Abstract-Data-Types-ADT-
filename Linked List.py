class ListNode:
    def __init__(self):
        self.Data = ""
        self.Next = 0

List = [ListNode() for i in range(5)]
Head = -1
Tail = -1
Free = 0

def initialize():
    global List, Head, Tail, Free
    for i in range(5):
        List[i].Data = ""
        List[i].Next = i + 1
    List[4].Next = -1
    Head = -1
    Tail =-1
    Free = 0

def InsertNode(Value):
    global List, Head, Tail, Free
    Temp = -1
    PrevNode = -1

    if Free == -1:
        print("List is Full")
    elif Free == 0:
        List[Free].Data = Value
        Head = Free
        Tail = Free
        Free = List[Free].Next
        List[Tail].Next = -1
    else:
        List[Free].Data = Value
        if Value < List[Head].Data:
            Temp = Head
            Head = Free
            Free = List[Free].Next
            List[Head].Next = Temp
        elif Value > List[Tail].Data:
            Temp = Tail
            Tail = Free
            Free = List[Free].Next
            List[Tail].Next = -1
            List[Temp].Next = Tail
        else:
            Temp = Head
            while Value > List[Temp].Data:
                PrevNode = Temp
                Temp = List[Temp].Next
            List[PrevNode].Next = Free
            Free = List[Free].Next
            List[List[PrevNode].Next].Next = Temp

def DeleteNode(Value):
    global List, Free, Head, Tail
    PrevNode = -1
    Found = False
    if Head == -1:
        print("Under Flow, List is Empty")
    else:
        CurrNode = Head
        while List[CurrNode].Data != Value and List[CurrNode].Next != -1:
            PrevNode = CurrNode
            CurrNode = List[CurrNode].Next

        if List[CurrNode].Data == Value and CurrNode == Head:
            Head = List[CurrNode].Next
            List[CurrNode].Next = Free
            Free = CurrNode
            List[Free].Data = ""
        elif List[CurrNode].Data == Value and CurrNode == Tail:
            List[PrevNode].Next = -1
            Tail = PrevNode
            List[CurrNode].Next = Free
            Free = CurrNode
            List[Free].Data = ""
        elif List[CurrNode].Data == Value:
            List[PrevNode].Next = List[CurrNode].Next
            List[CurrNode].Next = Free
            Free = CurrNode
            List[Free].Data = ""
        else:
            print("Data Not Found")

def Search(Value):
    for i in range(5):
        if List[i].Data == Value:
            return i

def Display():
    print("DATA NEXT")
    for i in range(5):
        print(List[i].Data," ",List[i].Next)
    print("Header : ",Head)
    print("Tail : ",Tail)
    print("Free : ",Free)

initialize()
choice = 0
while choice != 5:
    print("1 : ADD DATA TO LIST")
    print("2 : DELETE DATA FROM LIST")
    print("3 : DISPLAY")
    print("4 : SEARCH DATA FROM LIST")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        Add = str(input("Enter Value to Add : "))
        InsertNode(Add)
    elif choice == 2:
        Delete = str(input("Enter Value to Delete : "))
        DeleteNode(Delete)
    elif choice == 3:
        Display()
    elif choice == 4:
        find = str(input("Enter Value to Search : "))
        Index = Search(find)
        print("Index : ",Index)
    elif choice == 5:
        print("Exitting...")
    else:
        print("Invalid Choice")


