#ifndef CAR_H
#define CAR_H

#include <string>

class Car {
private:
    std::string maker;
    std::string color;
    int model;

public:
    // Constructor
    Car();

    // Getter and setter functions
    std::string getMaker() const;
    void setMaker(const std::string& maker);

    string setColor(string colors) {
        colors = color;
    };
    std::string getColor() {
        return colors;
    };

    int getModel() const;
    void setModel(int model);
};


#endif // CAR_H
