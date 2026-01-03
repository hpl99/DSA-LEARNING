#include<stdio.h>
int main(){
    int t;
    scanf("%d",&t);
    while(t--){
        int n;
        scanf("%d",&n);
        if(n%3==0){
            printf(" 0\n");
        }
        else{
           int x = n%3;
           if(x==1){
               printf("2\n");
           }
           else{
              printf("1\n");
           }
        }
    }
}