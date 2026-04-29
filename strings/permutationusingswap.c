#include<stdio.h>
#include<string.h>
void swap(char *a,char *b)
{
    char t = *a;
    *a=*b;
    *b=t;
}
void perm(char *s,int l,int h){
        int i;
        if(l==h){
           printf("%s\n",s);
        }
        else{
            for(i=l;i<=h;i++){
                 swap(&s[l],&s[i]);
                perm(s,l+1,h);
                swap(&s[l],&s[i]);
            }
        }
}
int main(){
    char s[100];
    scanf("%s",s);
    int x = strlen(s);
    perm(s,0,x-1);
    return 0;
}