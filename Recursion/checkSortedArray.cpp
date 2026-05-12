#include <bits/stdc++.h>
using namespace std;

#define fast_io ios::sync_with_stdio(false); cin.tie(nullptr);
#define endl '\n'
#define int long long
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define pb push_back
#define ff first
#define ss second

#ifdef LOCAL
    #define debug(x) cerr << #x << " = " << x << endl;
#else
    #define debug(x)
#endif

const int INF = 1e18;
const int MOD = 1e9 + 7;

using pii = pair<int,int>;
using vi = vector<int>;
using vvi = vector<vi>;

int mod_add(int a, int b, int m = MOD) { return (a + b) % m; }
int mod_mul(int a, int b, int m = MOD) { return (a * b) % m; }
int mod_pow(int a, int b, int m = MOD) {
    int res = 1;
    while (b > 0) {
        if (b & 1) res = (res * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return res;
}
bool helper (int num1,int num2)
{
    return num1<=num2;
}
bool checkArray(vector<int> arr){
    int i=1;
    while(i!=arr.size()-1)
    {
       bool  x = helper(arr[i-1],arr[i]);
        if(x==false){
            return false;
        }
        i++;
    }
    return true;
}
int32_t main() {
    fast_io;
    vector<int> nums = {1,2,8,15,66};
    cout <<  checkArray(nums);
}