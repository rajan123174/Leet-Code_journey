#include<iostream>
#include<map>
using namespace std;

int main () {
    map<int, string> m; // creating a map with integer keys and string values

    // Inserting key-value pairs into the map
    m[1] = "One";
    m[2] = "Two";
    m[3] = "Three";

    // Using insert function to add more key-value pairs
    m.insert({4, "Four"});
    m.insert(make_pair(5, "Five"));

    // Accessing and printing values using keys
    cout << "Key 1: " << m[1] << endl;
    cout << "Key 3: " << m.at(3) << endl; // using at() method

    // Iterating through the map and printing all key-value pairs
    cout << "All key-value pairs in the map:" << endl;
    for (const auto &pair : m) {
        cout << pair.first << " : " << pair.second << endl;
    }

    // Checking if a key exists in the map
    int keyToFind = 2;
    if (m.find(keyToFind) != m.end()) {
        cout << "Key " << keyToFind << " found with value: " << m[keyToFind] << endl;
    } else {
        cout << "Key " << keyToFind << " not found in the map." << endl;
    }

    // Removing a key-value pair from the map
    m.erase(4); // removing the pair with key 4

    cout << "Map after erasing key 4:" << endl;
    for (const auto &pair : m) {
        cout << pair.first << " : " << pair.second << endl;
    }

    multimap<int, string> mm; // creating a multimap
    mm.insert({1, "One"});
    mm.insert({1, "Uno"}); // inserting another value with the same key
    mm.insert({2, "Two"});
    cout << "All key-value pairs in the multimap:" << endl;
    for (const auto &pair : mm) {
        cout << pair.first << " : " << pair.second << endl;
    }


    unordered_map<string, int> um; // creating an unordered map
    um["Apple"] = 1;
    um["Banana"] = 2;
    um["Orange"] = 3;

    cout << "All key-value pairs in the unordered map:" << endl;
    for (const auto &pair : um) {
        cout << pair.first << " : " << pair.second << endl;
    }

    return 0;
}