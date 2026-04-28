#include<iostream>
#include<vector>
using namespace std;

class  Node
{
    public:
    int data ;
    Node* left , *right;

    Node(int key){
        data = key;
        left = nullptr;
        right = nullptr;
    }
};

void inorder(vector <int>& r,Node * node){
    if(node == nullptr){
        return ;
    }
    inorder (r,node->left);

    r.push_back(node->data);

    inorder(r,node->right);

}

void preorder(vector <int>& r,Node * node){
    if (node == nullptr){
        return ;
    }

    r.push_back(node->data);

    preorder(r,node->left);

    preorder(r,node->right);
}

void postorder(vector <int>& r,Node * node){
    if(node == nullptr){
        return ;
    }
    postorder(r,node->left);

    postorder(r,node->right);

    r.push_back(node->data);
}




int main()
{ 

    Node* fnode = new Node(2);
    Node* snode = new Node(3);
    Node* tnode = new Node(4);
    Node* ffnode =new Node(5);
    fnode->left  = snode;
    fnode->right = tnode;
    tnode->right = ffnode;

    vector<int> r;
    inorder(r,fnode);
    preorder(r,fnode);
    postorder(r,fnode);

    for(int node:r)
    {
        cout << node << endl;
    }

}