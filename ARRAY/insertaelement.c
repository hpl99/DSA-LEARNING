#include<stdio.h>
int main(){
    int arr[17]={1,5,6,8,7,6,9,3,11,25,3,9,599,5,54};
    for(int i=16;i>9;i--)
    {
        arr[i]=arr[i-1];
    }
    arr[9]=12;
    for(int i=0;i<16;i++)
    {
        printf("%d ",arr[i]);
    }
}