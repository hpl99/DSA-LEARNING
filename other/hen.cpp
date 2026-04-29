#include<iostream>
using namespace std;
int main()
{
    long long count = 0;
    for(long long i=1;i<=563000;i=i+2){
        count=count+i*i;
    }
    cout << count << endl;
}