#include<iostream>
using namespace std;

class Node{
public:
    int data;
    Node* next;

    Node(int val){
        data = val;
        next = NULL;
    }
};

class List{
    Node* head;
    Node* tail;

public:
    List() {
        head = tail = NULL;
    }
// push_front to add at the front
    void push_front(int val) {
        Node* newNode = new Node(val);
        if (head == NULL){
            head = tail = newNode;
            return;
        }
        else{
            newNode->next = head;
            head = newNode;
        }
    }
// push_back(val) to add at end
    void push_back(int val) {
        Node* newNode = new Node(val);

        if (head == NULL){
            head = tail = newNode;
        }else{
            tail->next = newNode;
            tail = newNode;
        }
    }
// pop_front() to delete from front
    void pop_front(){
        if (head == NULL){
            cout<< "the Linked List is emplty" << endl;
            return;
        }
        Node* temp = head;
        head = head->next;
        temp->next = NULL;
        delete temp;
    }

// pop_back() to delete from end
    void pop_back() {
        if (head == NULL){
            return;
        }

        Node* temp = head;
        while( temp->next != tail){
            temp = temp->next;
        }
        temp->next = NULL;
        delete tail;
        tail = temp;
    }

// insert(val,pos) to insert at an particular position 
    void insert(int val, int pos){
        if (pos <0) {
            return;
        }
        if (pos == 0){
            push_front(val);
        }

        Node* temp = head;
        for (int i=0; i<pos-1; i++){
            if(temp == NULL){
                cout<< "invalid pos\n";
                return;
            }
            temp = temp->next;
        }
        Node* newNode = new Node(val);
        newNode->next = temp->next;
        temp->next = newNode;
    }

// search(key) to search any particular element/ key
    int search(int key) {
        Node* temp = head;
        int idx = 0;

        while(temp != NULL){
            if (temp->data == key){
                return idx;
            }

            temp = temp->next;
            idx++;
        }

        return -1; 
    }


    void printLL() {
        Node* temp = head;

        while(temp != NULL){
            cout<< temp->data << "->";
            temp = temp->next;
        }
        cout << "NULL" << endl; 
    }
};

int main() {
    List ll;
    ll.push_front(3);
    ll.push_front(2);
    ll.push_front(1);
    ll.insert(2,2);



    ll.printLL();
    cout<< ll.search(0)<< endl;
}