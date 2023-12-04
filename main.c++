#include <iostream>
#include <string>
#include "Car.h"
using namespace std;


int main() {
    Car c1;
    c1.setMaker("Toyota");
    c1.setColor("Red");
    c1.setModel(2015);
    cout << "Maker: " << c1.getMaker() << endl;
    cout << "Color: " << c1.getColor() << endl;
    cout << "Model: " << c1.getModel() << endl;
    return 0;
}