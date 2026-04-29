#include<stdio.h>
int main(){
    char s[100];
    scanf("%s",s);
    long int h=0,x=0;
        int count = 0;

    for(int i=0;s[i]!=0;i++)
    {
        x= 1;
        x=x<<(s[i]-97);
        count++;
          if((x&h)){ 
            printf("%c is duplicate and repeated %d times \n ",s[i],count);
        }
        else {
          h =x|h;
        }
    }
    
}