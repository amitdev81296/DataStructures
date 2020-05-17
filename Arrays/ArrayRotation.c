#include <stdio.h>

void printArray(int arr[]) {
    int i;
    for(i=0;i<5;i++) {
        printf("%d ", arr[i]);
    }
}

void leftRotate(int arr[], int d) {
    int i, j;
    int temp;
    for(i=0;i<d;i++) {
        temp = arr[0];
        for(j=1;j<5;j++) {
            arr[j-1] = arr[j];
        }
        arr[4] = temp;
    }
    printArray(arr);
}

int main() {
    int arr[] = {1,2,3,4,5};
    int d;
    d = 3;
    printf("Original Array : ");
    printArray(arr);
    printf("\nRotated Array : ");
    leftRotate(arr, d);
}

