#include <stdio.h>

int main() {
	// your code goes here
	int t ;
	scanf("%d",&t);
	while(t--){
	    int n ;
	    scanf("%d",&n);
	    int arr1[1<<n];
	    int arr[n];
	    for(int i=0;i<n;i++)
	    {
	        scanf("%d",&arr[i]);
	    }
	    int k = 0;
        int y = 0;
	    for(int mask = 0;mask<(1<<n);mask++){
	        int count = 0;
	        for(int i=0;i<n;i++){
	            if(mask&(1<<i)){
	                count^=arr[i];
	            }
	        }
	       arr1[mask]=count; 
	    }
	    int count1 =0;
      for(int i=0;i<(1<<n);i++)
      {       
          if(arr1[i]>count1){
              count1=arr1[i];
          }
      }
      printf("%d\n",count1);
	}
}
