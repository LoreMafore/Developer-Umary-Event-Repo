#include <stdio.h>
#include <stdlib.h>

// BST implementation - incomplete
// Struggling with recursive functions

typedef struct TreeNode {
    int data;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

TreeNode* createNode(int data) {
    TreeNode* node = (TreeNode*)malloc(sizeof(TreeNode));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

TreeNode* insert(TreeNode* root, int data) {
    if (root == NULL) {
        return createNode(data);
    }
    
    if (data < root->data) {
        root->left = insert(root->left, data);
    } else if (data > root->data) {
        root->right = insert(root->right, data);
    }
    
    return root;
}

void inorderTraversal(TreeNode* root) {
    if (root != NULL) {
        inorderTraversal(root->left);
        printf("%d ", root->data);
        inorderTraversal(root->right);
    }
}

// TODO: implement search function
// TreeNode* search(TreeNode* root, int key) {
//     // confused about base case
// }

// TODO: implement delete function
// This one is really hard, not sure how to handle all cases
// TreeNode* deleteNode(TreeNode* root, int key) {
    
// }

// TODO: add function to find min/max
// TODO: add function to calculate height

int main() {
    TreeNode* root = NULL;
    
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 70);
    insert(root, 20);
    insert(root, 40);
    
    printf("Inorder traversal: ");
    inorderTraversal(root);
    printf("\n");
    
    // FIXME: no cleanup - memory leak
    
    return 0;
}
