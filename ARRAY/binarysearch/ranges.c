#include <stdio.h>
int main() {
    int arr[] = {1, 2, 5, 6, 8, 9, 11, 22, 145};
    int n = sizeof(arr) / sizeof(arr[0]);
    int a = 145;
    int b = 2;
    int l = -1, r = n;
    while (r > l + 1)
     {
        int m = (l + r) / 2;
        if (arr[m] < a) 
        {
            l = m;
        } 
        else 
        {
            r = m;
        }
    }
    int y = r;
    l = -1; r = n;
    while (r > l + 1) 
    {
        int m = (l + r) / 2;
        if (arr[m] < b) 
        {
            l = m;
        } 
        else 
        {
            r = m;
        }
    }
    int x = r;
    printf("%d",y-x);
    return 0;
}
