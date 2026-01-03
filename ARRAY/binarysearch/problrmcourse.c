#include<stdio.h>
int main(){
    int n , k;
    scanf("%d %d",&n,&k);
    int arr[n],arr1[k];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
     for(int i=0;i<k;i++)
    {
        scanf("%d",&arr1[i]);
    }
    for(int i=0;i<k;i++){
        int j=0;
    int l=0,h=n-1;
    int found = 0;
        int target = arr1[i];
    while(l<=h )
    {
         int m=(l+h)/2;
        if(arr[m]==target){
            found = 1;
            break;
        }
        else if(target>arr[m]){
            l=m+1;
        }
        else{
            h=m-1;
        }
    }
    if(found){
        printf("YES\n");
    }
    else{
        printf("NO\n");
    }
}
}