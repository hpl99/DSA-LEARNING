#include<stdio.h>
int main(){
    char s [100];
   // scanf("%s",s);
   fgets(s, sizeof(s), stdin);
    int hash[122]={0};
    int i=0;
    for(i = 0;s[i]!='\0';i++)
    {
        if(s[i]>=97 && s[i]<=122)
        {
        hash[s[i]-97]+=1; // for small letters 
        }
        else if(s[i]>=65 && s[i]<=90)
        {
            hash[s[i]-65]+=1; // for capital letters 
        }
        else if(s[i]>=48 && s[i]<=57)
        {
            hash[s[i]-48]+=1;// for numbers 
        }
    }
    for(i=0;i<26;i++){
        if(hash[i]>1){
            printf("%c  %c %c \n",i+97,i+65,i+47);
            printf("%d \n",hash[i]);
        }
    }
}