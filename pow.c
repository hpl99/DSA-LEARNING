#include<stdio.h>
int powerss(int x,int y){
    if(y==0){
        return 1;
    }
        return powerss(x,y-1)*x;
}
int main()
{
int x = powerss(2,14);
printf("%d",x);
}