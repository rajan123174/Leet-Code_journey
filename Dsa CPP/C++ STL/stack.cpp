#include<iostream>
#include<vector>
using namespace std;

int main () {
    stack<int> s; // creating a stack of integers
    s.push(10); // pushing elements onto the stack
    s.push(20);
    s.push(30);
    cout << "Top element: " << s.top() << endl; // accessing the top element
    s.pop(); // removing the top element
    cout << "Top element after pop: " << s.top() << endl; // accessing
    cout << "Size of stack: " << s.size() << endl; // getting the size of the stack
    while (!s.empty()) { // checking if the stack is empty
        cout << s.top() << " "; // printing and removing elements from the stack
        s.pop();
    }
    cout<< endl;
    return 0;
}