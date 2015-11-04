package com.winston.structures.binaryTree;

public class BinaryTree {

    Node root;

    public void put(int key, String value){
       Node node = new Node(key, value);

       if(root == null){
           root = node;
       }  else {
           Node focusNode = root;
           Node parent;
           while (true){
               parent = focusNode;
               if(key < focusNode.key){
                   focusNode = focusNode.leftChild;
                   parent.leftChild = node;
                   return;
               } else {
                   focusNode = focusNode.rightChild;
                   if(focusNode == null){
                       parent.rightChild = node;
                       return;
                   }
               }
           }
       }
    }


}
