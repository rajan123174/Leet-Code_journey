#include<iostream>
#include<queue>
using namespace std;

int main () {
    // Creating a max heap priority queue
    priority_queue<int> maxHeap;

    // Adding elements to the max heap
    maxHeap.push(10);
    maxHeap.push(5);
    maxHeap.push(20);
    maxHeap.push(15);

    cout << "Max Heap elements (in descending order): ";
    while (!maxHeap.empty()) {
        cout << maxHeap.top() << " "; // accessing the largest element
        maxHeap.pop(); // removing the largest element
    }
    cout << endl;

    // Creating a min heap priority queue
    // here we are using greater<int> to create a min heap
    // it acts as a functor to compare the elements
    priority_queue<int, vector<int>, greater<int>> minHeap;

    // Adding elements to the min heap
    minHeap.push(10);
    minHeap.push(5);
    minHeap.push(20);
    minHeap.push(15);

    cout << "Min Heap elements (in ascending order): ";
    while (!minHeap.empty()) {
        cout << minHeap.top() << " "; // accessing the smallest element
        minHeap.pop(); // removing the smallest element
    }
    cout << endl;

    return 0;
}