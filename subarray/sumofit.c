#include<stdio.h>
int main(){
    int n ;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
   int k = 3;
   int count = 0;
   for(int i=0;i<k;i++)
   {
    count+=arr[i];
   }
   int windowsum = count;
for(int i=k;i<n;i++){
    windowsum =windowsum +arr[i]-arr[i-k];
    if(windowsum>count){
        count = windowsum;
    }
     printf("i=%d, window_sum=%d, max_sum=%d\n", i, windowsum, count);
}
printf("%d",count);
}