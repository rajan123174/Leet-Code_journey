// stack using stl library
// we will use this in coding platform for submitting the solutions 

#include<iostream>
#include<stack>
using namespace std;

int main () {
    stack<int>s;

    s.push(10);
    s.push(20);
    s.push(30);

    while(!s.empty()) {
        cout << s.top() << " ";
        s.pop();
    }
    cout << endl; // 30 20 10
    return 0;
}
