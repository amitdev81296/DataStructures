from colorama import Fore, Style

class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity
    def enqueue(self, data):
        if len(self.queue) == self.capacity:
            return "QUEUE_FULL"
        self.queue = self.queue + [data]
        return "ENQUEUE_SUCCESSFUL"
    def dequeue(self):
        if len(self.queue) == 0:
            return "QUEUE_EMPTY"
        elif len(self.queue) == 1:
            self.queue = []
            return "DEQUEUE_SUCCESSFUL"
        else:
            temp = []
            for i in range(1, len(self.queue)):
                temp = temp + [self.queue[i]]
            self.queue = temp
            return "DEQUEUE_SUCCESSFUL"
    def peek(self):
        if len(self.queue) == 0:
            return "QUEUE_EMPTY"
        return self.queue[0]
    def display_queue(self):
        if len(self.queue) == 0:
            print(Fore.RED + "\nDisplay Error\nQueue Currently Empty.\n" + Style.RESET_ALL)
        else:
            result = "\nFRONT"
            for i in self.queue:
                result = result + " " + str(i)
            result = result + " REAR\n"
            print(Fore.YELLOW + result + Style.RESET_ALL)
            
print("\n***** Welcome To Queue Ops*****\n")
capacity = int(input("Enter the queue capacity : "))
queue = Queue(capacity)
option = 1
while option != 0:
    print("\n***** Queue Ops Menu *****")
    print("1. Enqueue.")
    print("2. Dequeue.")
    print("3. Peek.")
    print("4. Display Queue")
    print("5. Exit.")
    choice = int(input("\nEnter your choice : "))
    if choice == 1:
        data = int(input("\nEnter the data : "))
        message = queue.enqueue(data)
        if message == "QUEUE_FULL":
            print(Fore.RED + "\nEnqueue Error\nReason: Queue Full\n" + Style.RESET_ALL)
        elif message == "ENQUEUE_SUCCESSFUL":
            print(Fore.GREEN + "\nEnqueue Successful\n" + Style.RESET_ALL)
    elif choice == 2:
        message = queue.dequeue()
        if message == "QUEUE_EMPTY":
            print(Fore.RED + "\nDequeue Error\nReason: Queue Empty\n" + Style.RESET_ALL)
        elif message == "DEQUEUE_SUCCESSFUL":
            print(Fore.GREEN + "\nDequeue Successful\n" + Style.RESET_ALL)
    elif choice == 3:
        result = queue.peek()
        if result == "QUEUE_EMPTY":
            print(Fore.RED + "\nPeek Error\nReason: Queue Empty\n" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "\nPeek Result : ", result, ".\n" + Style.RESET_ALL)
    elif choice == 4:
       queue.display_queue()
    else:
        option = 0
