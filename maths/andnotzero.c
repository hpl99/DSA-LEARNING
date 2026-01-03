#include <stdio.h>
int main() {
    int nums[] = {1, 2, 3};
    int n = 3;
    printf("[");
    for(int mask = 0; mask < (1 << n); mask++) 
    {
        int c = ~0;
        int hasElement = 0;
        for(int i = 0; i < n; i++) 
        {
            if(mask & (1 << i)) 
            {
                c &= nums[i];
                hasElement = 1;
            }
        }
        if(hasElement && c > 0) {
            printf("{");
            int first = 1;
            for(int i = 0; i < n; i++) {
                if(mask & (1 << i)) {
                    if(!first) printf(",");
                    printf("%d", nums[i]);
                    first = 0;
                }
            }
            printf("},");
        }
    }
    printf("]\n");
    return 0;
}
