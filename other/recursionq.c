#include<stdio.h>
int factorial(int x){
    if(x==0){
        return 0;
    }
    else if(x==1){
        return 1;
    }
    int count = factorial(x-1)+factorial(x-2);
    return count;
}
int main()
{
    int y = factorial(12);
    printf("%d",y);
}