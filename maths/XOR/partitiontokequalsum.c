#include<stdio.h>
int main(){
    int nums[]={4,3,2,3,5,2,1};
    int k = 4;
    int arr[1<<7];
     
    for(int mask = 0;mask<(1<<7);mask++){
       int count = 0;
       //printf("{");
        for(int i=0;i<7;i++){
            if(mask&(1<<i))
            {
            // printf("%d",nums[i]);
             count+=nums[i];
            }
        }
        arr[mask]=count;
        //printf("}\n");    
    }
    for(int i=0;i<(1<<7);i++){
        int x = 0;
        for(int j=i+1;j<(1<<7)-1;j++){
            if(arr[i]==arr[j])
            {
                x++;
                if(x==k)
                {
                printf("true");
                }
            else{
                printf("false");
            }
            }
            
        }
    }
}