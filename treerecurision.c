#include<stdio.h>
void fu(int x){
    if(x>0){
    printf("%d\n",x);
    fu(x-1);
    fu(x-1);
}
}
int main()
{
    fu(3);
    return 0;
}