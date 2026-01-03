#include<stdio.h>
int main(){
    int arr[6]={1,2,1,3,2,5};
    int x = 0;
    for(int i=0;i<6;i++)
    {
        x^=arr[i];
    }
  int z = 0;
  int y= 0;
    int right = (x&(x-1))^x;
    for(int i=0;i<6;i++){
        if((arr[i]&right))
        {
            z^= arr[i];
        }
        else{
            y^= arr[i];
        }
    }
    printf("%d %d",z,y);
}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* singleNumber(int* nums, int numsize, int* returnsize) {
    int *arr = (int*) malloc(numsize*sizeof(int));
    if(!arr){
        return NULL;
    }
     unsigned int  x = 0;
     for(int i=0;i<numsize;i++)
    {
        x^=nums[i];
    }
    int z = 0;
    int y= 0;
   unsigned int right =x&(-x);
    for(int i=0;i<numsize;i++){
        if((nums[i]&right))
        {
            z^= nums[i];
        }
        else{
            y^= nums[i];
        }
    }
    arr[0]=z;
    arr[1]=y;
    *returnsize = 2;
    return arr;
}