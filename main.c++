#include <iostream>
#include <string>

using namespace std;

class Student {
    public: 
        string name;
        int age;
        int score;
        void say() {
            cout << "name: " << name << " age: " << age << " score: " << score << endl;
        };
        Student(string name, int age, int score) {
            this->name = name;
            this->age = age;
            this->score = score;
            name = "Test";
        };
};
int main() {
    Student stu("frocode", 15, 92);
    stu.say();
    Student stu2(stu.name, 16, 93);
    stu2.say();
    return 0;

};