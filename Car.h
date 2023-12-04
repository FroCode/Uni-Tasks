// Car.h
#pragma once  // Include guard to prevent multiple inclusions

#include <string>
using namespace std;
class Car
{
private:
    string maker;
    string color;
    int model;

public:
    Car();
    void setmaker(string maker);
    void setcolor(string color);
    void setmodel(int model);
    string getmaker();
    string getcolor();
    int getmodel();
    



};
