#include<iostream>
#include<vector>
#include<algorithm> // for std::next_permutation
using namespace std;


int main() {
    vector<int> vec = {1, 2, 3};


    cout << "Original vector: ";
    for (int val : vec) {
        cout << val << " ";
    }
    cout << endl;

    


    // Generating the next permutation
    if (next_permutation(vec.begin(), vec.end())) {
        cout << "Next permutation: ";
        for (int val : vec) {
            cout << val << " ";
        }
        cout << endl;
    } else {
        cout << "No next permutation available." << endl;
    }

    // Generating previous permutation
    if (prev_permutation(vec.begin(), vec.end())) {
        cout << "Previous permutation: ";
        for (int val : vec) {
            cout << val << " ";
        }
        cout << endl;
    } else {
        cout << "No previous permutation available." << endl;
    }

    

    
    return 0;

}