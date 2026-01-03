#include<stdio.h>
int main()
{
    int arr[8]={1,8,9,12,33,54,741,3222};
    int l = 0,m= 0,h=7;
    int key = 3222;
    m=(l+h)/2+1;
    int mid = arr[m];
    for(int i=0;i<8;i++)
    {
        if(key>mid){
            l = m+1;
            m=(l+h)/2;
            mid =arr[m];
        }
        else if(key<mid)
        {
            h=m-1;
            m=(l+h)/2;
            mid=arr[m];
        }
        else{
            printf("%d",m);
            break;
        }
    }
}