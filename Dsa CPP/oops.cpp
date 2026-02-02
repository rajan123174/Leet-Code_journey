#include<iostream>
#include<string>
using namespace std;


class Teacher {
public:
    string name;
    string dept;
    double salary;

    // parametarized constructor
    Teacher(string name, string dept, double salary){
        this-> name = name;
        this-> dept = dept;
        this-> salary = salary;
    }


    // copy constructor 
    Teacher(Teacher &orgObj) {
        cout<< "I am, custom copy constructor"<<endl;
        this-> name = orgObj.name;
        this-> dept = orgObj.dept;
        this-> salary = orgObj.salary;
    }

    

    void changeDept(string newDept){
        dept = newDept;
    }
};

int main(){
    Teacher t1("rajan","cse",12000);
    //cout<< t1.name << " " <<t1.dept << " " <<t1.salary << endl;

    Teacher t2(t1); // custom copy constructor called;
    cout<< t2.name << " " <<t2.dept << " "<< t2.salary << endl; 
    
    return 0;
}