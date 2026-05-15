#include <bits/stdc++.h>
using namespace std;

void selcsort(vector<int>& arr ,int r , int c,int max ){
    if(r==0){
        return ;
    }
    if(c<r){
    if(arr[c]>arr[max]){
        selcsort(arr,r,c+1,c);
    }
    else{
        selcsort(arr,r,c+1, max);
    }
}
else{
    int temp = arr[max ];
    arr[max]= arr[r-1];
    arr[r-1] = temp;
    selcsort(arr,r-1,0,0);
}
}

int32_t main() {
    vector<int> arr = {1,4,2,5,8,7};
    selcsort(arr,arr.size(),0,0);
    for(int i=0;i<6;i++){
        cout << arr[i] << " ";
    }
}