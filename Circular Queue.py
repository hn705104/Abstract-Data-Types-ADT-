#ADT QUEUE
CircularQueue = [None for i in range(8)]
HeadPointer = -1 #Used to remove/Dequeue Data
TailPointer = -1 #Used to add/Enqueue Data
Qlen = len(CircularQueue)
Qsize = 0

#Procedure to initialize the Queue
def initialize():
    global HeadPointer, TailPointer, Qlen, Qsize
    HeadPointer = -1
    TailPointer = -1
    Qsize =0
    for i in range(Qlen):
        CircularQueue[i] = 0

#Code for Enqueue
def Enqueue(Data):
    global HeadPointer, TailPointer, Qlen, Qsize
    if Qsize == Qlen:
        print("Overflow, Queue is full")
    elif TailPointer == len(CircularQueue)-1:
        TailPointer = 0
    else:
        TailPointer += 1
    CircularQueue[TailPointer] = Data
    Qsize += 1

#Code for Dequeue
def Dequeue():
    global HeadPointer, TailPointer, Qlen, Qsize
    if Qsize == 0:
        print("Underflow, Queue is Empty")
        return None
    elif HeadPointer == len(CircularQueue)-1:
        HeadPointer = 0
    else:
        HeadPointer += 1
    RData = CircularQueue[HeadPointer]
    Qsize -= 1
    return RData

#Code for Display of Queue
def DisplayCircularQueue():
    print("Queue Length: ",Qlen)
    print("Queue Size: ",Qsize)
    print("Head Pointer: ",HeadPointer)
    print("Tail Pointer: ",TailPointer)
    print()
    print("Queue: ",CircularQueue)
    print()

#main Program
initialize()
choice = 0
while choice != 4:
    print("To Enqueue data in a Queue: 1")
    print("To Dequeue data in a Queue: 2")
    print("To Display a Queue: 3")
    print("To Exit the program: 4")
    choice = int(input("Enter your Choice: "))
    if choice == 1:
        QData = input("Enter Data to input: ")
        Enqueue(QData)
    elif choice == 2:
        QData = Dequeue()
        if QData != None:
            print("Dequeued Element is: ",QData)
        else:
            initialize()
    elif choice == 3:
        DisplayCircularQueue()
    elif choice ==4:
        break
    else:
        print("invalid choice")




