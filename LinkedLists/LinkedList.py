class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def display_list(self):
        if self.head == None:
            print("\nThe linked list is currently empty.")
        else:
            n = self.head
            while n != None:
                if n.next == None:
                    print(n.data)
                else:
                    print(n.data, " -> ", end=" ")
                n = n.next
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.next != None:
                n = n.next
            n.next = new_node
        print("\n****Data Insertion Successful****")
        self.display_list()
    
    def delete_from_end(self):
        if self.head == None:
            print("\nUnable to delete from empty list")
        else:
            to_be_deleted_node = self.head
            second_last_node = self.head
            while to_be_deleted_node.next != None:
                second_last_node = to_be_deleted_node
                to_be_deleted_node = to_be_deleted_node.next
            if to_be_deleted_node == self.head:
                self.head = None
            else:
                second_last_node.next = None
            print("\n*****Data Deletion Successful****")
            self.display_list()


linked_list = LinkedList()
option = 1
while option != 0:
    print("\n*****Linked List Operations*****")
    print("1. Display List.")
    print("2. Insert At End.")
    print("3. Delete From End.")
    print("4. Exit.")
    choice = int(input("\nEnter your choice : "))
    if choice == 1:
        linked_list.display_list()
    elif choice == 2:
        data = int(input("\nEnter the data to be inserted : "))
        linked_list.insert_at_end(data)
    elif choice == 3:
        linked_list.delete_from_end()
    else:
        option = 0
