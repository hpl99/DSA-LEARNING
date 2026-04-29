#include<stdio.h>
int main(){
    char a[100];
    char b[100];
    scanf("%s %s",a,b);
    int i,j;
    for(i=0,j=0;a[i]!='\0',b[i]!='\0';i++,j++){
        if(a[i]!=b[j]){
            break;
        }
    }
    // THis cAN also be an algorithm for dictionary probelm as you find lesser and 
    // greater sooooo 
        if(a[i]==b[j]){
            printf("Equla");
        }
        else if(a[i]>b[j]){
            printf("lessesr");
        }
        else{
            printf("greater");
        }
}