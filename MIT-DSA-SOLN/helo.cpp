#include <bits/stdc++.h>
using namespace std;
#define fast_io ios::sync_with_stdio(false); cin.tie(nullptr);
#define endl '\n'
#define int long long
struct node{
    int data;
    struct node *next;
};
int32_t main() {
    fast_io;
    int n;
    cin >> n;
    struct node *head = NULL;
    struct node *tail = NULL;
    struct node *nn = NULL;
    struct node *nt = NULL;
    for(int i = 0; i < 2*n; i++) {
        node *temp = new node();
        temp->data = i;
        temp->next = NULL;
        // second half (insert at beginning)
        if(i >= n){
            temp->next = nn;
            nn = temp;
        }
        else{
            // first half normal
            if(head == NULL){
                head = temp;
                tail = temp;
            }
            else{
                tail->next = temp;
                tail = temp;
            }
        }
    }
    // attach reversed second half
    tail->next = nn;
    // print
    node *f = head;
    while(f != NULL){
        cout << f->data << " ";
        f = f->next;
    }

    return 0;
}