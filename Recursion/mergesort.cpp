#include <bits/stdc++.h>
using namespace std;

void mergesort(vector<int>& arr, int l, int r){

    if(l >= r){
        return;
    }

    int m = (l + r) / 2;

    // Sort left half
    mergesort(arr, l, m);

    // Sort right half
    mergesort(arr, m + 1, r);

    // Merge step
    vector<int> temp;

    int i = l;
    int j = m + 1;

    while(i <= m && j <= r){

        if(arr[i] <= arr[j]){
            temp.push_back(arr[i]);
            i++;
        }
        else{
            temp.push_back(arr[j]);
            j++;
        }
    }

    while(i <= m){
        temp.push_back(arr[i]);
        i++;
    }

    while(j <= r){
        temp.push_back(arr[j]);
        j++;
    }

    // Copy back
    for(int k = l; k <= r; k++){
        arr[k] = temp[k - l];
    }
}

int main(){

    vector<int> arr = {5,2,8,1,3};

    mergesort(arr, 0, arr.size() - 1);

    for(int x : arr){
        cout << x << " ";
    }
}