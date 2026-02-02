#include<iostream>
#include<list>
using namespace std;

int main () {
    list<int> l; // creating a list of integers

    // Adding elements to the list
    l.push_back(10); // adds 10 at the end
    l.push_back(20); // adds 20 at the end
    l.push_front(5); // adds 5 at the front

    cout << "Elements in the list: ";
    for (int val : l) {
        cout << val << " "; // prints the elements of the list
    }
    cout << endl;

    // Removing elements from the list
    l.pop_back(); // removes the last element (20)
    l.pop_front(); // removes the first element (5)

    cout << "Elements in the list after popping: ";
    for (int val : l) {
        cout << val << " "; // prints the remaining elements of the list
    }
    cout << endl;

    // Inserting an element at a specific position
    auto it = l.begin(); // iterator pointing to the first element
    l.insert(it, 15); // inserts 15 before the first element

    cout << "Elements in the list after insertion: ";
    for (int val : l) {
        cout << val << " "; // prints the elements of the list
    }
    cout << endl;

    return 0;
}