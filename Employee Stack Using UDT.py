class EmployeeRec:
    def __init__(self):
        self.EmployeeID = None
        self.EmployeeName = None
        self.EmployeeSalary = None

EmployeeStack = [EmployeeRec() for i in range(10)]
null = -1
TopPointer = null

def initStack():
    global EmployeeStack, TopPointer
    for i in range(10):
        EmployeeStack[i].EmployeeID = null
        EmployeeStack[i].EmployeeName = ""
        EmployeeStack[i].EmployeeSalary = 0.0
    TopPointer = null

def Push(Value):
    global TopPointer,EmployeeStack
    if TopPointer == len(EmployeeStack)-1:
        print("Stack OverFlow")
    else:
        TopPointer += 1
        EmployeeStack[TopPointer].EmployeeID = Value.EmployeeID
        EmployeeStack[TopPointer].EmployeeName = Value.EmployeeName
        EmployeeStack[TopPointer].EmployeeSalary = Value.EmployeeSalary

def Pop():
    global TopPointer,EmployeeStack
    Value = EmployeeRec()
    if TopPointer == null:
        print("Stack Underflow")
        return null
    else:
        Value.EmployeeID = EmployeeStack[TopPointer].EmployeeID
        Value.EmployeeName = EmployeeStack[TopPointer].EmployeeName
        Value.EmployeeSalary = EmployeeStack[TopPointer].EmployeeSalary
        TopPointer -= 1
        return Value

def Display():
    global TopPointer,EmployeeStack
    if TopPointer == null:
        print("Stack is Empty")
    else:
        print("EMPLOYEE ID","\t","EMPLOYEE NAME","\t","EMPLOYEE SALARY")
        for i in range(len(EmployeeStack)-1,null,-1):
            if i == TopPointer:
                print(EmployeeStack[i].EmployeeID,"\t",EmployeeStack[i].EmployeeName,"\t",EmployeeStack[i].EmployeeSalary,"\t <---- TOP")
            else:
                print(EmployeeStack[i].EmployeeID,"\t",EmployeeStack[i].EmployeeName,"\t",EmployeeStack[i].EmployeeSalary)

initStack()
choice = 0
Data = EmployeeRec()
while choice != 4:
    print("1 : Push the value on to the Stack")
    print("2 : Pop the value on to the Stack")
    print("3 : Display Stack")
    print("4 : Exit Program")
    choice = int(input("Enter Your choice : "))
    if choice == 1:
        Data.EmployeeID = input("Enter Employee ID : ")
        Data.EmployeeName = input("Enter Employee Name : ")
        Data.EmployeeSalary = input("Enter Employee Salary : ")
        Push(Data)
    elif choice == 2:
        Data = Pop()
        if Data != null:
            print("Employee ID : ",Data.EmployeeID)
            print("Employee Name : ",Data.EmployeeName)
            print("Employee Salary : ",Data.EmployeeSalary)
    elif choice == 3:
        Display()
    elif choice == 4:
        print("Exitting...")
    else:
        print("INVALID CHOICE")



