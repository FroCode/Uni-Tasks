#include <iostream>
#include <string>

using namespace std;

class Student {
    public: 
        string name;
        int age;
        int score;
        static int count;
        void say() {
            cout << "name: " << name << " age: " << age << " score: " << score << endl;
        };
        Student(string name, int age, int score) {
            this->name = name;
            this->age = age;
            this->score = score;
            name = "fr";
        };
};
int main() {
    Student stu("fr", 15, 92);
    stu.say();
    Student stu2(stu.name, 16, 93);
    Student st3("fr", 15, 92);
    st3.count = 10;
    return 0;

};