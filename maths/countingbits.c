#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    printf("[");

    int arr[n + 1];
    for (int i = 0; i <= n; i++) {
        arr[i] = i;
    }

    for (int j = 0; j <= n; j++) {
        int count = 0;
        for (int i = 0; i < 32; i++) { 
            if (arr[j] & (1 << i)) {
                count++;
            }
        }
        printf("%d", count);
        if (j != n) printf(", ");
    }

    printf("]");
    return 0;
    // int* countBits(int n, int* returnSize) {
    // int *arr = (int*)malloc((n + 1) * sizeof(int));

    // for (int j = 0; j <= n; j++) {
    //     int count = 0;
    //     for (int i = 0; i < 32; i++) { // check all 32 bits
    //         if (j & (1ULL << i)) {
    //             count++;
    //         }
    //     }
    //     arr[j] = count;
    // }

    // *returnSize = n + 1;
    // return arr;
}
