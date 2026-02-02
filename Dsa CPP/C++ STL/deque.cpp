#include<iostream>
#include<deque>
using namespace std;

int main() {
    deque<int> d; // creating a deque of integers

    // Adding elements to the deque
    d.push_back(10); // adds 10 at the end
    d.push_back(20); // adds 20 at the end
    d.push_front(5); // adds 5 at the front

    cout << "Elements in the deque: ";
    for (int val : d) {
        cout << val << " "; // prints the elements of the deque
    }
    cout << endl;

    // Removing elements from the deque
    d.pop_back(); // removes the last element (20)
    d.pop_front(); // removes the first element (5)

    cout << "Elements in the deque after popping: ";
    for (int val : d) {
        cout << val << " "; // prints the remaining elements of the deque
    }
    cout << endl;

    // Inserting an element at a specific position
    auto it = d.begin(); // iterator pointing to the first element
    d.insert(it, 15); // inserts 15 before the first element

    cout << "Elements in the deque after insertion: ";
    for (int val : d) {
        cout << val << " "; // prints the elements of the deque
    }
    cout << endl;

    cout<< "First element: " << d.front() << endl; // gives first element
    cout<< "first element:" << d[0] << endl; // gives first element
    cout<< "Last element: " << d.back() << endl; // gives last element

    return 0;
}