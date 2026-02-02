#include<iostream>
#include<vector>
#include<iterator> // for using iterators
using namespace std;



int main(){
    vector<int> v = {10, 20, 30, 40, 50};

    // Creating an iterator to traverse the vector
    vector<int>::iterator it = v.begin(); // iterator pointing to the first element

    cout << "Elements in the vector using iterator: ";
    while(it != v.end()) { // iterate until the end of the vector
        cout << *it << " "; // dereference the iterator to get the value
        ++it; // move to the next element
    }
    cout << endl;

    // Using reverse iterator to traverse the vector in reverse order
    vector<int>::reverse_iterator rit = v.rbegin(); // reverse iterator pointing to the last element

    cout << "Elements in the vector in reverse order using reverse iterator: ";
    while(rit != v.rend()) { // iterate until the beginning of the vector
        cout << *rit << " "; // dereference the reverse iterator to get the value
        ++rit; // move to the previous element
    }
    cout << endl;


    vector<int>::iterator itr;
    for (itr = v.begin(); itr != v.end();itr++) {
        cout << *(itr) << " "<< endl;
    }


    for (auto itr = v.rbegin(); itr != v.rend(); itr++) {
        cout << *(itr) << " "<< endl;
    }

    return 0;
}