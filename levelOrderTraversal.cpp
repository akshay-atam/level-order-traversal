#include <iostream>
using namespace std;
 
// Data structure to store a binary tree node
struct Node
{
    int key;
    Node *left, *right;
 
    Node(int key)
    {
        this->key = key;
        this->left = this->right = nullptr;
    }
};
 
// Function to print all nodes of a given level from left to right
bool printGivenLevel(Node* root, int level)
{
    if (root == nullptr) {
        return false;
    }
 
    if (level == 1)
    {
        cout << root->key << " ";
 
        // return true if at least one node is present at a given level
        return true;
    }
 
    bool left = printGivenLevel(root->left, level - 1);
    bool right = printGivenLevel(root->right, level - 1);
 
    return left || right;
}
 
// Function to print level order traversal of a given binary tree
void printLevelOrderTraversal(Node* root)
{
    // start from level 1 — till the height of the tree
    int level = 1;
 
    // run till `printGivenLevel()` returns false
    while (printGivenLevel(root, level)) {
        level++;
    }
}
 
int main()
{
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->left = new Node(6);
    root->right->right = new Node(7);
 
    printLevelOrderTraversal(root);
 
    return 0;
}