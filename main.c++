#include <iostream>
#include <string>

using namespace std;

class Rec {
public:
    int area(int a, int b) {
        return a * b;
    }
};

class Sq : public Rec {
public:
    int vol(int a, int b, int c) {
        return a * b * c;
    }
};

int main() {
    int a;
    cout << "Hello World!" << endl;
    Sq s;

    // Correcting the usage of the area function
    cout << s.area(2, 3) << endl;

    // Correcting the usage of cin and endl
    cin >> a;
    cout << s.area(3, 5) << endl;
    cout << s.vol(3, 4, 5) << endl;

    return 0;
}
