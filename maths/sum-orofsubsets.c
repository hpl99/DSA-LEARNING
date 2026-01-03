 #include<stdio.h>
 int main(){
 int nums[]={1,2,2};
 int max = 0;
 int count = 0;
 int arr[50];
          
    for(int mask = 0;mask<(1<<3);mask++){
          int cmask =0;
         cmask |= mask;
         printf("{");
        for(int i=0;i<3;i++) 
        {
        if(mask & (1<<i)) 
        { 
          printf(" %d ",nums[i]);
         
        }
         arr[mask]=cmask;
        
        if(cmask>max)
       {   
        max= cmask;
       }   
    }
 printf("} ");
}
// for(int i=0;i<3;i++){
//     if(arr[i]==max)
//     {
//         count++;
//     }
// }
// printf("%d",count);
}