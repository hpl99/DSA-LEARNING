#include<stdio.h>
#include <stdlib.h>
struct node {
    int data;
    struct node *next;
}*s;

// creation of fn for ll
void create (int a[],int n){
    struct node *p,*last;
    s = (struct node *)malloc(sizeof(struct node));
    s->data = a[0];
    s->next = NULL;
    last = s;
    
    for (int i=1;i<n;i++){
        p = (struct node*)malloc(sizeof(struct node));
        p->data = a[i];
        p->next = NULL;
        last->next =p;
        last = p;
    }
}

void display(struct node *s){
    while(s->next!=NULL){
        printf("%d -> ",s->data);
        s=s->next;
    }
}

int main(){
    int a[6]={1,2,3,8,9,7};
    create(a,7);
    display(s);
    printf("NULL");
}
