from colorama import Fore, Style

class Stack:
    def __init__(self, capacity):
        self.stack_array = []
        self.top = 0
        self.capacity = capacity
    def show_stack(self):
        if len(self.stack_array) == 0:
            print(Fore.YELLOW + "\nThe Stack Appears To Be Empty\nPlease Push Some Data.\n" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "\nTOP")
            for i in self.stack_array:
                print(i)
            print("BOTTOM\n" + Style.RESET_ALL)
    def pop(self):
        if len(self.stack_array) == 0:
            return "STACK_EMPTY"
        else:
            data = self.stack_array[self.top]
            new_stack_array = []
            if len(self.stack_array) == 1:
                self.stack_array = new_stack_array
            else:
                for i in range(1, len(self.stack_array)):
                    new_stack_array = new_stack_array + [self.stack_array[i]]
                self.stack_array = new_stack_array
            return data

    def push(self, data):
        if len(self.stack_array) == capacity:
            return "STACK_OVERFLOW"
        else:
            if len(self.stack_array) == 0:
                self.stack_array = [data]
            else:
                new_stack_array = [data]
                for i in range(0, len(self.stack_array)):
                    new_stack_array = new_stack_array + [self.stack_array[i]]
                self.stack_array = new_stack_array
            return "PUSH_SUCCESSFUL"

    def peek(self):
        if len(self.stack_array) == 0:
            return "STACK_EMPTY"
        return self.stack_array[0]

print("\n***** Welcome To Stack Ops*****\n")
capacity = int(input("Enter the stack capacity : "))
stack = Stack(capacity)
option = 1
while option != 0:
    print("\n***** Stack Ops Menu *****")
    print("1. Pop.")
    print("2. Push.")
    print("3. Peek.")
    print("4. Display Stack")
    print("5. Exit.")
    choice = int(input("\nEnter your choice : "))
    if choice == 1:
        result = stack.pop()
        if result == "STACK_EMPTY":
            print(Fore.RED + "\nPop Operation Failed.\nReason: Empty Stack\n" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "\nPop Operation Successful.\nPopped Element : ", result, "\n" + Style.RESET_ALL)
    elif choice == 2:
        result = stack.push(int(input("\nEnter Data To Be Pushed : ")))
        if result == "STACK_OVERFLOW":
            print(Fore.RED + "\nPush Operation Failed.\nReason: Stack Overflow" + Style.RESET_ALL)
        elif result == "PUSH_SUCCESSFUL":
            print(Fore.GREEN + "\nPush Operation Successful.\n" + Style.RESET_ALL)
    elif choice == 3:
        result = stack.peek()
        if result == "STACK_EMPTY":
            print(Fore.RED + "\nPeek Operation Failed.\nReason: Empty Stack\n" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "\nPeek Operation Successful.\nElement At Stack Top : ", result, "\n" + Style.RESET_ALL)
    elif choice == 4:
        stack.show_stack()
    else:
        option = 0
