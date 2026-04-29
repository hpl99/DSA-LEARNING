#include<stdio.h>
#include<string.h>
int main(){
 int t;
 scanf("%d",&t);
 while(t--){
    int n;
    scanf("%d",&n);
    char s[n+1];
    scanf(" %s",s);
    int count = 0;
    int count1 = 0;
    for(int i=0;s[i]!='\0';i++){
        if(s[i]=='a')
        {
            count++;
        }
        else
        {
            count1++;
        }
    }
    int y = count+count1;
    printf("%d",y);
 }
}