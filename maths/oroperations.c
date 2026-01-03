#include<stdio.h>
int main()
{
    char s[5]={'a','b','c','d'};
      int cmask =0;
    for(int mask= 0;mask<(1<<4);mask++)
    {
      
        cmask |= mask;
        printf("{");
        for(int i=0;i<4;i++)
        {
            if(cmask&(1<<i))
            {
                printf("%c",s[i]);
            }
        }
        printf("} \n");
    }
}