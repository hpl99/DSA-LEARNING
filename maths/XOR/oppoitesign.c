#include<stdio.h>
int main(){
    int x = -5;
    int y = -3;
    int count = 0;
    if(x&((1<<8)))  // CORRECT AND SIMPLE WAY IS XOR OF TWO NUM LIKE X^Y<0 DIFF
    {
        count++;
    }
    if(y&((1<<8)))
    {
        count++;
    }
    if(count== 1){
        printf("opposite");
    }
    else{
        printf("same");
    }
}