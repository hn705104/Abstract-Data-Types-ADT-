class StRec:
    def __init__(self):
        self.StID = None
        self.StName = None
        self.StFee = None

Stack = [StRec() for i in range(10)]
null = -1
TopPointer = null

def initStack():
    for i in range(10):
        Stack[i].StID = null
        Stack[i].StName = ""
        Stack[i].StFee = 0.0
        TopPointer = null


def push(Value):
    global TopPointer,Stack
    if TopPointer == len(Stack) -1:
        print("Stack overflow")
    else:
        TopPointer += 1
        Stack[TopPointer].StID = Value.StID
        Stack[TopPointer].StName = Value.StName
        Stack[TopPointer].StFee = Value.StFee


def pop():
    global Stack,TopPointer
    Ans = StRec()
    if TopPointer == null:
        print("Stack Underflow")
    else:
        Ans.StID = Stack[TopPointer].StID
        Ans.StName = Stack[TopPointer].StName
        Ans.StFee = Stack[TopPointer].StFee
        TopPointer -= 1
        return Ans

def Display():
    global TopPointer,Stack
    if TopPointer == null:
        print("Stack is Empty")
    else:
        for i in range(len(Stack)-1,null,-1):
            if i == TopPointer:
                print(Stack[i].StID,Stack[i].StName,Stack[i].StFee,"\t <---- Top")
            else:
                print(Stack[i].StID,Stack[i].StName,Stack[i].StFee)

initStack()
choice = 0
Data = StRec()
while choice != 4:
    print("STACK MENU")
    print("1 : Push value onto the Stack")
    print("2 : Pop the value from the Stack")
    print("3 : Display Stack")
    print("4 : Exit Program")
    choice = int(input("Enter your Choice : "))
    if choice == 1:
        Data.StID = input("Enter Student ID : ")
        Data.StName = input("Enter Student Name : ")
        Data.StFee = input("Enter Student Fee : ")
        push(Data)
    elif choice == 2:
        Data = pop()
        print("Student ID : ",Data.StID)
        print("Student Name : ",Data.StName)
        print("Student Fee : ",Data.StFee)
    elif choice == 3:
        Display()
    elif choice == 4:
        print("Exitting...")
    else:
        print("Invalid Choice ")
