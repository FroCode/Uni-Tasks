#include <iostream>
#include <string>

using namespace std;

class Rec {
public:
    int area(int a, int b) {
        return a * b;
    }
    int test(int a, int b) {
        return a * b;
    }
};

class Sq : public Rec {
public:
    int vol(int a, int b, int c) {
        return a * b * c;
    }
    int test(int a, int b) {
        return a + b;
    }

};

int main() {
    int a;
    cout << "Hello World!" << endl;
    Sq s;
    cout << s.test(3, 4) << endl;

    return 0;
}
