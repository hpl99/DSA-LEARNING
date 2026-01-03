#include<stdio.h>
int main(){
    char s[3]={'a','b','c'};
    int cmask = 0;
    for(int mask = 0;mask<(1<<3);mask++){
        cmask|=mask;
        printf("{");
        for(int i=0;i<4;i++)
        {
            if(cmask & (1<<i))
            {
                printf("%c",s[i]);
            }
        }
        printf("} \n");
    }
    return 0;
}