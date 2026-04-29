#include<stdio.h>
int main(){
    char s[100];
    int t=0;
    scanf("%s",s);
    int j=0;
    for( j=0;s[j]!='\0';j++)
    {
    }
    j= j-1;
        for(int i=0;i<j;i++,j--)
        {
            if(s[i]==s[j]){
                t=1;
            }
            else{
                break;
            }
        }
        if(t){
    printf(" yes this is a palindrome %s \n",s);
        }
        else{
printf("no panindirme \n");
        }
}