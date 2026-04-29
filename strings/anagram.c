// this strings have same characters but diffrent order and meaning and length
//is obvouisly the same for ex medical decimal
// using hash map

#include<stdio.h>
int main(){
    char s[100];
    char b[100];
    scanf("%s %s",s,b);
    int i=0;
    int h[128]={0};
    for( i=0;s[i]!='\0';i++){
        h[s[i]]++;
    }
    for(i=0;b[i]!='\0';i++){
        h[b[i]]--; 
        if(h[b[i]]<0)
        {
            printf("Not Aangram \n");
            return 0;
        }
    }
   if(b[i]=='\0')
   {
        printf("I t i s a a n a g r a m");
    }
    return 0;
}