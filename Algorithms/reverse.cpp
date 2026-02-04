// to reverse the array or vectors 

#include <iostream>
#include <vector>
#include <algorithm> // for std::reverse
using namespace std;


int main () {
    vector<int> vec = {1, 2, 3, 4, 5};

    cout << "Original vector: ";
    for (int val : vec) {
        cout << val << " ";
    }
    cout << endl;

    // Reversing the vector using std::reverse
    reverse(vec.begin(), vec.end());

    cout << "Reversed vector: ";
    for (int val : vec) {
        cout << val << " ";
    }
    cout << endl;

    return 0;
}