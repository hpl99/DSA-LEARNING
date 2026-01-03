#include <stdio.h>
#define N 4
#define MAX_MASK (1 << N)

int main() {
    int nums[] = {1,2,3,4};
    int k = 3;
    int subset_sum[MAX_MASK] = {0};
    int sum_count[1000] = {0};  // Use large enough array to count subset sums

    // Step 1: Compute all subset sums
    for (int mask = 1; mask < MAX_MASK; mask++) {
        int sum = 0;
        for (int i = 0; i < N; i++) {
            if (mask & (1 << i)) {
                sum += nums[i];
            }
        }
        subset_sum[mask] = sum;
        sum_count[sum]++;
        
        // Early exit: if any sum appears k times
        if (sum_count[sum] >= k) {
            printf("true\n");
            return 0;
        }
    }

    printf("false\n");
    return 0;
}
