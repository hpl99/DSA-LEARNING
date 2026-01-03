#include<stdio.h>
int main(){
    int n =16;
    if((n&(n-1))==0){
        printf("true");
    }
    else{
        printf("false");
    }
}