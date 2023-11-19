#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <ctime>

    class BST {
        struct 
        Node* root = nullptr;
        void addHelper(int value, Node* temp); 
        int getMaxHelper(Node* temp);
        int getMinHelper(Node * temp);
        public:
            void add(int value);
            int getMax();
            int getMin();
            void display_order() {
        if(root == nullptr) return;
        queue<Node*> q;
        q.push(root);
        while (!q.empty()) {
            Node* temp = q.front();
            q.pop();
            cout << temp->data << " ";
            if(temp->left != nullptr) {
                q.push(temp->left);
            }
            if(temp->right != nullptr) {
                q.push(temp->right);
            }
        }
        
    }
    return 0;
        
    }

    int main() {
        BST obj;
        obj.add(15);
        obj.add(6);
        obj.add(20);
        obj.add(3);
        obj.add(9);
        obj.add(8);
        obj.add(25);
        display_order();
    }

    
}
