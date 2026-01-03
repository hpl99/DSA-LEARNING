#include<stdio.h>
void add(int x){
    if(x>0){
        add(x-1);
        printf("%d \n",x);
    }
}
int main(){
    int x;
    add(5);
}