#include<iostream>
#include<queue>
using namespace std;

int main() {
    queue<int> q; // creating a queue of integers

    // Adding elements to the queue
    q.push(10); // adds 10 at the back
    q.push(20); // adds 20 at the back
    q.push(30); // adds 30 at the back

    cout << "Front element: " << q.front() << endl; // accessing the front element
    cout << "Back element: " << q.back() << endl; // accessing the back element
    cout << "Size of queue: " << q.size() << endl; // getting the size of the queue

    // Removing elements from the queue
    q.pop(); // removes the front element (10)

    cout << "Front element after pop: " << q.front() << endl; // accessing the new front element
    cout << "Size of queue after pop: " << q.size() << endl; // getting the new size of the queue

    // Emptying the queue
    while (!q.empty()) { // checking if the queue is empty
        cout << q.front() << " "; // printing and removing elements from the queue
        q.pop();
    }
    cout << endl;

    return 0;
}