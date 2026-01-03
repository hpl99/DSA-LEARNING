#include<iostream>
#include<algorithm>
using namespace std;

bool isgood(long long t, int n, int x, int y) {
    if (t < min(x, y))
        return false;

    long long cnt = 1;
    t -= min(x, y);
    cnt += t / x + t / y;
    return cnt >= n;
}

int main() {
    int n, x, y;
    cin >> n >> x >> y;

    long long l = 0, r = 1LL * max(x, y) * n, mid;

    while (r > l + 1) {
        mid = (l + r) / 2;
        if (isgood(mid, n, x, y))
            r = mid;
        else
            l = mid;
    }

    cout << r;
}
