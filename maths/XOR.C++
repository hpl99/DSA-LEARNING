#include<iostream>
#include<stdio.h>
using namespace std ; 
int main(){
    int arr[9]= {1,1,2,2,3,4,3,4,6};
    int unique = 0;
    for(auto arrs : arr)
    {
        unique ^= arrs; 
    }
    cout << unique ;
}