#include<iostream>
#include<utility> // for using pair
using namespace std;


int main() {
    pair<int, string> p; // creating a pair of integer and string

    p.first = 1; // assigning value to the first element of the pair
    p.second = "Hello"; // assigning value to the second element of the pair

    cout << "First element: " << p.first << endl; // printing the first element
    cout << "Second element: " << p.second << endl; // printing the second element

    pair<int, string> p2 = make_pair(2, "World"); // creating and initializing a pair using make_pair

    cout << "First element of p2: " << p2.first << endl; // printing the first element of p2
    cout << "Second element of p2: " << p2.second << endl; // printing the second element of p2

    // Swapping two pairs
    p.swap(p2);

    cout << "After swapping:" << endl;
    cout << "First element of p: " << p.first << endl; // printing the first element of p after swap
    cout << "Second element of p: " << p.second << endl; // printing the second element of p after swap
    cout << "First element of p2: " << p2.first << endl; // printing the first element of p2 after swap
    cout << "Second element of p2: " << p2.second << endl; // printing the second element of p2 after swap


    vector<pair<int, string>> vec = {{1, "One"}, {2, "Two"}, {3, "Three"}}; // vector of pairs
    vec.push_back({4, "Four"}); // adding a new pair to the vector
    vec.emplace_back(5, "Five"); // adding a new pair using emplace_back
    for (auto pr : vec){
        cout << pr.first << " : " << pr.second << endl;
    }
    return 0;
}