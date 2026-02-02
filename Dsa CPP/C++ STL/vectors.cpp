#include<iostream>
#include<vector>
using namespace std;


int main(){
    vector<int> v;

    v.push_back(10); // these are the functions to add elements in vector
    v.push_back(20);
    v.push_back(30);


// both push_back and emplace_back are used to add elements at the end of the vector
    v.emplace_back(40); // more efficient way to add elements and called an alternative to push_back


    v.pop_back(); // removes the last element from the vector
    v.pop_back();

    //v.begitn(); // returns an iterator to the first element
    //v.end(); // returns an iterator to the element following the last element
    v.erase(v.begin()); // removes the element at the specified position, here it removes the first element
    v.insert(v.begin(), 5); // inserts an element at the specified position, here it inserts 5 at the beginning

    for(int val : v) { // this is for each loop
        cout << val << " ";
    }
    cout << endl; // 10 20 30

    //cout<< "Value at 1st index: " << v.at(1) << endl; // gives value at 1st index
    //cout<< "value at 0th index: " << v[0] << endl; // gives value at 0th index
    //cout<< "first element: " << v.front() << endl; // gives first element
    cout<< "last element: " << v.back() << endl; // gives last element
    return 0;
}