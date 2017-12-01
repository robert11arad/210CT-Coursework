/*
Title: Doubly Linked Lists Implementation
Author : Hintea, D.
Date : 2017
Availability : http ://moodle.coventry.ac.uk

Title : Delete a node from Binary Search Tree
Author : mycodeschool
Date : 2014
Availability : https://www.youtube.com/watch?v=gcULXE7ViZw
*/

#include "stdafx.h"
#include <iostream>

class BinTreeNode {
public:
	BinTreeNode(int value) {
		this->value = value;
		this->left = NULL;
		this->right = NULL;
	}
	int value;
	BinTreeNode* left;
	BinTreeNode* right;

};

BinTreeNode* tree_insert(BinTreeNode* tree, int item) {
	if (tree == NULL)
		tree = new BinTreeNode(item);
	else
		if (item < tree->value)
			if (tree->left == NULL)
				tree->left = new BinTreeNode(item);
			else
				tree_insert(tree->left, item);
		else
			if (tree->right == NULL)
				tree->right = new BinTreeNode(item);
			else
				tree_insert(tree->right, item);
	return tree;

}

void postorder(BinTreeNode* tree) {
	if (tree->left != NULL)
		postorder(tree->left);
	if (tree->right != NULL)
		postorder(tree->right);
	std::cout << tree->value << std::endl;

}

void in_order(BinTreeNode* tree) {
	if (tree->left != NULL)
		in_order(tree->left);
	std::cout << tree->value << std::endl;
	if (tree->right != NULL)
		in_order(tree->right);
}

//Find the adress to the node with the smallest value.
BinTreeNode* FindMin(BinTreeNode* root)
{
	while (root->left != NULL) root = root->left;
	return root;
}

BinTreeNode* Delete(BinTreeNode* root, int data) {
	if (root == NULL) return root;
	//Goes through the left subtree and deletes the given value once it find it.
	else if (data < root->value) root->left = Delete(root->left, data);
	//Goes through the right subtree and deletes the given value once it find it.
	else if (data > root->value) root->right = Delete(root->right, data);
	else {
		// Case 1:  No child
		if (root->left == NULL && root->right == NULL) {
			delete root;//Dealocate memory.
			root = NULL;//Allocate 0 to root memory adress.
		}
		//Case 2: One child
		else if (root->left == NULL) {
			BinTreeNode *temp = root;//Temporary pointer.
			root = root->right;//Makes the right child the new root.
			delete temp;//Deletes the initial root.
		}
		else if (root->right == NULL) {
			BinTreeNode *temp = root;//Temporary pointer.
			root = root->left;//Makes the left child the new root.
			delete temp;//Deletes the initial root.
		}
		//Case 3: 2 children
		else {
			BinTreeNode *temp = FindMin(root->right);//Saves in a temporary pointer the smalles value in the right subtree.
			root->value = temp->value;//Sets the value of the root to the temporary pointer value.
			root->right = Delete(root->right, temp->value);//Removes the temporary value.
		}
	}
	return root;
}

int main(int argc, char *argv[])
{
	BinTreeNode* t = tree_insert(0, 6);
	tree_insert(t, 10);
	tree_insert(t, 5);
	tree_insert(t, 2);
	tree_insert(t, 3);
	tree_insert(t, 4);
	tree_insert(t, 11);
	tree_insert(t, 11);
	Delete(t, 11);
	in_order(t);
	system("pause");
	return 0;
}