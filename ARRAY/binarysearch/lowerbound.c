#include<stdio.h>
int main(){
    int n , k;
    scanf("%d %d",&n,&k);
    int arr[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    for(int i=0;i<k;i++){
        int x ;
        scanf("%d",&x);
        int j=0;
    int l=-1,h=n;
   while(h>l+1){
       int m = (l+h)/2;
       if(arr[m]<x){
           l=m;
       }
       else{
           h=m;
       }
   }
   if(h<n&&arr[h]==x)
   {
    printf("YES\n");
   }
   else{
    printf("NO\n");
   }
  // printf("%d\n",h+1);
}
}