#include <iostream>
#include <string>
using namespace std;
class Person{
private:
    string name;
    int age;
protected:
    string department;
public:
    Person();
    Person(string n, int a, string d){
        name = n;
        age = a;
        department = d;
    }
    void displayInfo(){
        cout<<"Name: "<<name<<endl;
        cout<<"Age: "<<age<<endl;
        cout<<"Department: "<<department<<endl;
    };
    string getRole() const{
        return "General Staff";
    }
};
class Lecturer:public Person{
private:
    string subject;
public:
    Lecturer();
    Lecturer(string n, int a, string d, string s):Person(n, a, d){
        subject = s;
    };
    string getRole() const{
        return "Lecturer";
    }
    void displayInfo(){
        Person::displayInfo();
        cout<<"Subject: "<<subject<<endl;
    }
    void assignDepartment(string dept){
        department = dept;
    };
};
int main() {
    Lecturer l1("John Smith", 35, "Computer Science", "Software Engineering");
    l1.assignDepartment("Information Technology");
    l1.displayInfo();
    cout << "Role: " << l1.getRole() << endl;
    return 0;
}
