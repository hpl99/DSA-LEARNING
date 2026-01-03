#include<stdio.h>
int main(){
    int arr[8]={1,2,4,5,6,8,7,9};
    arr[3]=0;
    for(int i=3;i<8;i++)
    {
        arr[i]=arr[i+1];
    }
    for(int i=0;i<8;i++)
    {
        printf("%d ",arr[i]);
    }
}