<?php

class Node
{
    public $value;
    public $left;
    public $right;

    public function __construct($value) {
        $this->value = $value;
        $this->left = null;
        $this->right = null;
    }
}

class BinaryTree
{
    public $root;

    public function __construct($root) {
        $this->root = new Node($root);
    }
}

$tree = new BinaryTree(1);
$tree->root->left = new Node(2);
$tree->root->right = new Node(3);
$tree->root->left->left = new Node(4);
$tree->root->left->right = new Node(5);
$tree->root->right->left = new Node(6);
$tree->root->right->right = new Node(7);
$tree->root->right->right->right = new Node(8);
