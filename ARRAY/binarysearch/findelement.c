#include<stdio.h>
int main(){
    int n ;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    int k;
    while(k--){
        int a , b;
        scanf("%d %d",&a,&b);
        int count = 0;
        for(int i=0;i<n;i++){
            int l = a;
            int h= b;
            while(h>l+1){
                int m  = (l+h)/2;
                if(arr[m]>=l){
                    count++;
                }
                else{
                    count++;
                }
            }
        }
        printf("%d",count);
    }
}