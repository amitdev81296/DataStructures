#include <stdio.h>

void printArray(int arr[]) {
    int i;
    for(i=0;i<5;i++) {
        printf("%d ", arr[i]);
    }
}

void reverseArray(int arr[]) {
    int reverse[5];
    int i, j;
    for(i=0;i<5;i++) {
        reverse[((i-5)*(-1))-1] = arr[i];
    }
    printArray(reverse);
}

int main() {
    int arr[] = {1,2,3,4,5};
    printf("Original Array : ");
    printArray(arr);
    printf("\nReversed Array : ");
    reverseArray(arr);
}