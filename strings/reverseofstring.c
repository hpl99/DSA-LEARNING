#include<stdio.h>
int main(){
    char s[100],t;
    scanf("%s",s);
    int j=0;
    for( j=0;s[j]!='\0';j++)
    {
    }
    j= j-1;
        for(int i=0;i<j;i++,j--)
        {
            t=s[i];
            s[i]=s[j];
            s[j]=t;
        }
    printf("%s",s);
}