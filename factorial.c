#include<stdio.h>
int factorial(int x){
    if(x==0){
        return 1;
    }
    return factorial(x-1)*x;
}
int main(){
    int x ;
    scanf("%d",&x);
    int  y= factorial(x);
    printf("%d",y);
}