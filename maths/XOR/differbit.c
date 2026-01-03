#include<stdio.h>
// HERE WE ARE FINDING THE RIGHTMOST DIFFRENT BIT
int main(){
    int a , b;
    scanf("%d %d",&a,&b);
    int count = 0;
    for(int i=0;i<(1<<3);i++){
        if((a&(1<<i))^(b&(1<<i)))
        {
            count++;;
            printf("%d",count);
            break;
        }
        else{
            count++;
        }
    }
}