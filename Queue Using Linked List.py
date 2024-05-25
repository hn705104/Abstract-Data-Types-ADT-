class Node:
    def __init__(self):
        self.Data = None
        self.Next = None

QueueList = [Node() for i in range(10)]
Head = -1
Tail = -1
Free = 0
Qsize = 0
Qlen = len(QueueList)

def initialize():
    global QueueList, Head, Tail, Free
    for i in range(10):
        QueueList[i].Data = ""
        QueueList[i].Next = i + 1
    QueueList[9].Next = -1
    Free = 0
    Head = -1
    Tail = -1

def Enqueue(Value):
    global QueueList, Head, Tail, Free
    if Free == -1:
        print("Queue OverFlow!")
    Temp = Free
    Free = QueueList[Free].Next
    QueueList[Temp].Data = Value
    QueueList[Temp].Next = -1
    if Head == -1:
        Head = Temp
    else:
        QueueList[Tail].Next = Temp
    Tail = Temp

def Dequeue():
    global QueueList, Head, Tail, Free
    if Head == -1:
        print("Under FLow!")
        return -1
    Temp = Head
    Head = QueueList[Head].Next
    if Head == -1:
        Tail = -1
    QueueList[Temp].Next = Free
    Free = Temp
    return QueueList[Temp].Data

def printQ():
    global Head, Tail, Free
    if Head == -1:
        print("Queue is empty")
        return
    temp = Head
    while temp != -1:
        print(QueueList[temp].Data, end=" ")
        temp = QueueList[temp].Next
    print()
    print("head: ", Head)
    print("tail: ", Tail)
    print("free: ", Free)

# main program
initialize()
choice = 0
while choice != 4:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Print")
    print("4. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = input("Enter data: ")
        Enqueue(data)
    elif choice == 2:
        data = Dequeue()
        print("Dequeued data: ", data)
    elif choice == 3:
        printQ()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
    print()


