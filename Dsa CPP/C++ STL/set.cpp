#include<iostream>
#include<set>
#include<unordered_set>
using namespace std;


int main() {
    set<int> s; // creating a set of integers

    // Inserting elements into the set
    s.insert(10);
    s.insert(20);
    s.insert(30);
    s.insert(20); // duplicate element, will not be added

    auto it = s.lower_bound(15);
    if (it != s.end()) {
        cout << "Lower bound of 15 is: " << *it << endl;
    } else {
        cout << "No lower bound found for 15." << endl;
    }

    cout << "Elements in the set: ";
    for (int val : s) {
        cout << val << " "; // prints the elements of the set
    }
    cout << endl;

    // Checking if an element exists in the set
    int elementToFind = 20;
    if (s.find(elementToFind) != s.end()) {
        cout << elementToFind << " found in the set." << endl;
    } else {
        cout << elementToFind << " not found in the set." << endl;
    }

    auto itr = s.upper_bound(20);
    if (itr != s.end()) {
        cout << "Upper bound of 20 is: " << *itr << endl;
    } else {
        cout << "No upper bound found for 20." << endl;
    }

    // Removing an element from the set
    s.erase(10); // removes the element 10

    cout << "Elements in the set after erasing 10: ";
    for (int val : s) {
        cout << val << " "; // prints the remaining elements of the set
    }
    cout << endl;

    multiset<int> ms; // creating a multiset of integers
    ms.insert(10);
    ms.insert(20);
    ms.insert(20); // duplicate element, will be added
    ms.insert(30);
    cout << "Elements in the multiset: ";
    for (int val : ms) {
        cout << val << " "; // prints the elements of the multiset
    }
    cout << endl;

    unordered_set<int> us; // creating an unordered set of integers
    us.insert(10);
    us.insert(20);
    us.insert(30);
    us.insert(20); // duplicate element, will not be added
    cout << "Elements in the unordered set: ";
    for (int val : us) {
        cout << val << " "; // prints the elements of the unordered set
    }
    cout << endl;

    return 0;
}