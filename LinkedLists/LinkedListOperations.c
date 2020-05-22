#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
}*head;

void displayList() {
    if(head == NULL) {
        printf("\nList is Empty\n");
    }
    else {
        struct Node *n;
        n = head;
        printf("\n");
        while (n != NULL) {
            if(n->next != NULL) {
                printf("%d -> ", n->data);
            }
            else {
                printf("%d\n", n->data);
            }
            n = n->next;
        }
    }
    return;
}

void insertAtEnd(int data) {
    struct Node *newNode, *temp;
    newNode = (struct Node *) malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    temp = head;
    if(temp != NULL) {
        while(temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
    else {
        head = newNode;
    }
    printf("\nData Insertion Successful\n");
    return;
}

void deleteFromEnd() {
    struct Node *toDelete, *secondLastNode;
    if(head == NULL) {
        printf("\nThe list is already empty.\n");
    }
    else {
        toDelete = head;
        secondLastNode = head;
        while(toDelete->next != NULL) {
            secondLastNode = toDelete;
            toDelete = toDelete->next;
        }
        if(toDelete == head) {
            head = NULL;
        }
        else {
            secondLastNode->next = NULL;
        }
        free(toDelete);
        printf("\nData Insertion Successful\n");
    }
    return;
}

int printMainMenu(struct Node *start) {
    int option = 1;
    head = (struct Node *) malloc(sizeof(struct Node));
    int dataForNodeOne;
    printf("\nEnter the data for the first node : ");
    scanf("%d", &dataForNodeOne);
    head->data = dataForNodeOne;
    head->next = NULL;
    while(option != 0) {
        printf("\n*****Linked List Operation Menu*****");
        printf("\n1. Display List.");
        printf("\n2. Insert At End.");
        printf("\n3. Delete From End.");
        printf("\n4. Exit.");
        printf("\nEnter Your Choice : ");
        int choice, data;
        scanf("%d", &choice);
        switch (choice)
        {
            case 1:
                displayList();
                break;
            case 2:
                printf("\nEnter the data : ");
                scanf("%d", &data);
                insertAtEnd(data);
                break;
            case 3:
                deleteFromEnd();
                break;
            default:
                option = 0;
        }
    }
    return 0;
}

int main() {
    struct Node *start = NULL;
    printMainMenu(start);
    return 0;
}