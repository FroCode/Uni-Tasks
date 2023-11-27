#include <iostream>
#include <string>

using namespace std;

class rectangle {
private:
    float length, width;

public:
    void setLength(float l) {
        if (l >= 0) {
            length = l;
        } else {
            cout << "Please enter a valid length" << endl;
        }
    }

    float getLength() {
        return length;
    }

    void setWidth(float w) {
        if (w >= 0) {
            width = w;
        } else {
            cout << "Please enter a valid width" << endl;
        }
    }

    float getWidth() {
        return width;
    }

    float getArea() {
        return length * width;
    }
};

int main() {
    rectangle r1;
    r1.setLength(10);
    r1.setWidth(5);
    cout << "Area: " << r1.getArea() << endl;
    return 0;
}
