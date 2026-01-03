#include<stdio.h>
#include<stdbool.h>
long long w,h,n;
bool good(long long x)
{
    return (x/w)*(x/h)>=n;
}
int main(){
    scanf("%lld %lld %lld ",&w,&h,&n);
    long long l =0; // l is bad 
    long long r = 1;  // r is good
    while(!good(r))
    {
        r=r*2;
    }
    while(r>l+1){
        long long m =(l+r)/2;
        if(good(m)){
            r=m;
        }
        else{
            l=m;
        }
    }
    printf("%lld\n",r);
   return 0;   
}