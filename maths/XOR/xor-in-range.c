#include <stdio.h>

int main() {
    int n = 50;    // 110010₂
    int l = 2, r = 4;

    for (int i = l; i <= r; i++) {
        n ^= (1 << (i - 1));  // Flip each bit one by one
    }

    printf("Result: %d\n", n);
    return 0;
}
