#include <bits/stdc++.h>
using namespace std;
void bubblesort(vector<int>& arr, int s, int e){
    if(s == 0){
        return;
    }
    if(e < s){

        if(arr[e] > arr[e + 1]){
            swap(arr[e], arr[e + 1]);
        }

        bubblesort(arr, s, e + 1);
    }
    else{
        bubblesort(arr, s - 1, 0);
    }
}
int main(){
    vector<int> arr = {1,3,2,5,4,6};
    bubblesort(arr, arr.size() - 1, 0);
    for(int x : arr){
        cout << x << " ";
    }
}