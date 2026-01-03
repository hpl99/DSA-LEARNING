#include<stdio.h>
int main(){
    int arr[5]={1,2,2};
    printf("[");
    for(int mask=0;mask<(1<<3);mask++){
        printf("[");
        for(int i=0;i<3;i++){
            if(mask&(1<<i))
            {
                printf("%d" ,arr[i]);
            }
        }
        printf("] \n");
    }
    return 0;
}